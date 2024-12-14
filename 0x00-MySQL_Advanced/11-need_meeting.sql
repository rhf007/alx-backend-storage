-- list of all students with score under 80 and no last_meeting or more than 1 month
CREATE OR REPLACE VIEW need_meeting AS SELECT name FROM students
WHERE score < 80 AND (last_meeting IS NULL OR
TIMESTAMPDIFF(MONTH, last_meeting, CURDATE()) > 1);
