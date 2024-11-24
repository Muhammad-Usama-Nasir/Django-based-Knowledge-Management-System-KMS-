from django.db import models

class Chapter(models.Model):
    title = models.CharField(max_length=255)  #Programming Language Syntax
    introduction = models.TextField()
    conclusion = models.TextField()

    def __str__(self):
        return self.title

class Section(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="sections")
    section_title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.section_title} - {self.chapter.title}"

class KeyConcept(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="key_concepts")
    concept = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.concept} - {self.chapter.title}"

class Example(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="examples")
    title = models.CharField(max_length=255)
    case_study = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.chapter.title}"
