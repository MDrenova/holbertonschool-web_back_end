/*eslint-disable*/
const getStudentIdsSum = (list) => list.reduce((total, student) => total + student.id, 0);

export default getStudentIdsSum;
// function getStudentIdsSum(list) {
//   var total = 0;
//   for (var i = 0; i < list.length; i++) {
//       total = total + list[i].id;
//   }
//   return total;
// }
