---
content_hash: 36612c2c386319209516d1b0683c550611d0286363085f86c23c827d539eabd4
fetched_at: '2026-06-29T00:09:35.491195+00:00'
page_id: '425459367'
product: rm
source: tdn-rm
title: TOTVS Gestão de Pessoas x Fluig LMS - Elearning - Cadastro Avaliação de Conhecimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459367
version: 3
---

**Avaliação de Conhecimento da Turma**

---

Para cadastrar uma Avaliação de conhecimento acesse RH | Gestão de Pessoas | Desenvolvimento | Turmas | Anexos | Avaliação de conhecimento.

As avaliações de conhecimento regulares e as avaliações de *Pré-Teste* e *Pós-Teste são diferenciadas pelo campo* "**TIPO**" (VTUAVCONH), relacionadas à integração de Cursos E*-Learning*.  As outras avaliações que não são desses tipos, serão definidas como *Regular.*  
    
Só poderá existir uma avaliação Pré-Teste e uma avaliação Pós-Teste em cada turma. Para avaliações do tipo Regular, não há restrição quanto à quantidade por Turma.  
    
Após sua criação as Avaliações do tipo Pré-Teste ou Pós-Teste não poderão ter o tipo alterado para Regular. Avaliações do tipo Regular poderão ser alteradas para Pré-Teste ou Pós-Teste, sempre respeitando a regra de haver apenas uma avaliação desse tipo por Turma.  
    
Para turmas que não sejam **Turma Integração *E-Learning***, o fluxo e a interface se manterão os mesmos.  
    
A tela de criação/edição de avaliação de conhecimento, irá bloquear a integração com **RM Testis** para avaliações do tipo Pré-Teste e Pós-Teste. Durante a criação ou edição de uma nova avaliação de conhecimento, se for marcado o checkbox para criar uma avaliação de Pré-Teste ou Pós-Teste, o sistema irá desabilitar o *lookup* "Prova RM Testis".       
    
       A rotina de recebimento de informações de execução de avaliação do LMS (SCORE) deverá ser tratada para que, quando receber uma nota de um e-learning vinculado a uma turma e avaliação de conhecimento, grave na tabela de notas de avaliação de conhecimento pré ou pós teste (**VTUAVCONH**) a nota obtida na avaliação do e-learning. Se o avaliado ainda não estiver na avaliação de conhecimento, deverá ser incluído neste momento. Gravar informação de aprovação em avaliação de conhecimento na tabela de matricula de turma e-learning.  
    
 **Observações:**  
    
 Quando uma avaliação for do tipo Pré-Teste ou Pós-Teste, os seguintes processos serão bloqueados:

* Gerar Inscrições no **RM Testis**;
* Recuperar Nota no **RM Testis**;

O script de criação do novo campo "**TIPO**" na tabela **VTUAVCONH**, irá atualizar toda as avaliações de conhecimento existente para o tipo 0 (zero), referente às avalições do tipo Regular.
