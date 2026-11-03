def puede_modificar(user,student_id,group_id,con):
    # TODO: solo profesor asignado al grupo Y estudiante inscrito en él.
    if not user or user['role'] != 'profesor':
        return False
    row = con.execute(
        '''
        SELECT 1
        FROM groups g
        JOIN enrollments e ON e.group_id = g.id
        WHERE g.id = ? AND g.professor_id = ? AND e.student_id = ?
        ''',
        (group_id, user['id'], student_id),
    ).fetchone()
    return row is not None

def puede_consultar(user,student_id,group_id,con):
    # TODO: estudiante propio e inscrito, o profesor asignado al grupo con estudiante inscrito.
    if not user:
        return False
    if user['role'] == 'profesor':
        return puede_modificar(user, student_id, group_id, con)
    if user['role'] == 'estudiante':
        if user['id'] != student_id:
            return False
        row = con.execute(
            'SELECT 1 FROM enrollments WHERE student_id = ? AND group_id = ?',
            (student_id, group_id),
        ).fetchone()
        return row is not None
    return False
