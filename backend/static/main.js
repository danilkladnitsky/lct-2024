// Инициализация сцены, камеры и рендера
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

//camera.position.z = 5;
camera.position.z = 5;
camera.position.x = 5;
camera.position.y = 2.5;

// Добавление освещения
const ambientLight = new THREE.AmbientLight(0x404040); // Окружающий свет
scene.add(ambientLight);

const pointLight = new THREE.PointLight(0xffffff, 1, 100);
pointLight.position.set(lightPosition.x, lightPosition.y, lightPosition.z);
scene.add(pointLight);

// Контроллеры для управления камерой
const controls = new THREE.OrbitControls(camera, renderer.domElement);

// Функция для создания объектов
function createObject(object) {
    let geometry;
    let material = new THREE.MeshPhongMaterial({ color: parseInt(object.color) });
    let mesh;

    switch(object.type) {
        case 'box':
            geometry = new THREE.BoxGeometry(object.size[0], object.size[1], object.size[2]);
            mesh = new THREE.Mesh(geometry, material);
            break;
        case 'polygon':
            console.log('create polygon')
            const shape = new THREE.Shape();
            object.points.forEach((point, index) => {
                if (index === 0) {
                    shape.moveTo(point.x, point.z); // Используем x и z координаты для плоскости XZ
                } else {
                    shape.lineTo(point.x, point.z); // Используем x и z координаты для плоскости XZ
                }
            });
            shape.lineTo(object.points[0].x, object.points[0].z); // Замыкаем форму
            const extrudeSettings = {
                steps: 2,
                depth: object.depth, // Глубина экструзии
                bevelEnabled: false
            };
            geometry = new THREE.ExtrudeGeometry(shape, extrudeSettings);
            mesh = new THREE.Mesh(geometry, material);
            mesh.rotation.x = Math.PI / 2;
            break;
        // Добавьте другие типы объектов по мере необходимости
        default:
            console.error('Unknown object type:', object.type);
            return;
    }

    mesh.position.set(object.position.x, object.position.y, object.position.z);
    scene.add(mesh);

    // Добавление контуров
//    const edges = new THREE.EdgesGeometry(geometry);
//    const line = new THREE.LineSegments(edges, new THREE.LineBasicMaterial({ color: 0x000000 }));
//    line.position.set(object.position.x, object.position.y, object.position.z);
//    scene.add(line);
}


// Создание объектов из переданных данных
objects.forEach(createObject);

// Добавление функции анимации
function animate() {
    requestAnimationFrame(animate);
    controls.update(); // Обновление контроллеров
    renderer.render(scene, camera);
}
animate();

function toRadians(angle) {
    return angle * (Math.PI / 180);
}

function toDegrees(angle) {
    return angle * (180 / Math.PI);
}
