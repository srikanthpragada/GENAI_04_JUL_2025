import sqlite3

def create_connection():
    try:
        conn = sqlite3.connect("courses.db")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_course(course_id, course_title, duration, fee):
    try:
        conn = create_connection()
        if conn is None:
            return False
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO COURSES (course_id, course_title, duration, fee) VALUES (?, ?, ?, ?)",
            (course_id, course_title, duration, fee)
        )
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error creating course: {e}")
        return False
    finally:
        if conn:
            conn.close()

def read_course(course_id):
    try:
        conn = create_connection()
        if conn is None:
            return None
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM COURSES WHERE course_id = ?",
            (course_id,)
        )
        row = cursor.fetchone()
        return row
    except sqlite3.Error as e:
        print(f"Error reading course: {e}")
        return None
    finally:
        if conn:
            conn.close()

def update_course(course_id, course_title=None, duration=None, fee=None):
    try:
        conn = create_connection()
        if conn is None:
            return False
        cursor = conn.cursor()
        updates = []
        params = []
        if course_title is not None:
            updates.append("course_title = ?")
            params.append(course_title)
        if duration is not None:
            updates.append("duration = ?")
            params.append(duration)
        if fee is not None:
            updates.append("fee = ?")
            params.append(fee)
        if not updates:
            print("No fields to update.")
            return False
        params.append(course_id)
        sql = f"UPDATE COURSES SET {', '.join(updates)} WHERE course_id = ?"
        cursor.execute(sql, params)
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error updating course: {e}")
        return False
    finally:
        if conn:
            conn.close()

def delete_course(course_id):
    try:
        conn = create_connection()
        if conn is None:
            return False
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM COURSES WHERE course_id = ?",
            (course_id,)
        )
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error deleting course: {e}")
        return False
    finally:
        if conn:
            conn.close()


