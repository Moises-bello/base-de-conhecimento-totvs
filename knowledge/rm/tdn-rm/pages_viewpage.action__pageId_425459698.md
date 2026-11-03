---
content_hash: 016d5de81c380105c3683b07c4ddf3ae43abc9ac2b06137aa49f3c1fcc5c94e5
fetched_at: '2026-06-29T00:09:38.059835+00:00'
page_id: '425459698'
product: rm
source: tdn-rm
title: Filiação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459698
version: 5
---

Nas versões anteriores, o TOTVS Educacional não se adequava ao conceito de multiparentalidade. Na guia "Responsáveis" só era possível cadastrar um pai e uma mãe para o aluno.  
    
 Para adequação do sistema ao conceito de multiparentalidade e parentalidade socioafetiva (em que uma pessoa pode ter mais de um pai ou mãe no seu registro civil), o cadastro de filiação passou a ser de responsabilidade do TOTVS Gestão de Pessoas, onde no cadastro de Pessoa possui o anexo Filiação que manipula a tabela VFILIACAO, este anexo também está vinculado ao cadastro de Aluno no TOTVS Educacional.  
    
 **Obs.** Afim de evitar impactos nos relatórios que já utilizavam os campos antigos SPESSOA.CODPESSOAPAI e SPESSOA.CODPESSOAMAE, sempre que for realizado um cadastro de filiação os dados serão replicados para os campos antigos, porém lembramos que com os campos antigos só é possível vincular uma mãe e um pai ao aluno, para que os relatórios utilizem o conceito de multiparentalidade deve-se atualiza-los para buscar os dados da tabela VFILIACAO.  
    
 No anexo Filiação é possível inserir pais e mães para o aluno, a partir do cadastro de pessoas feito no TOTVS Gestão de Pessoas e definir se essa(s) pessoa(s) é (são) pai(s) ou mãe (s) do aluno selecionado através da seção "Tipo de Relacionamento". Também é possível verificar se o pai ou mãe do aluno é falecido, este campo é apenas informativo e poderá ser alterado apenas no cadastro de pessoas.  
    
 Para que a usabilidade do cadastro de Alunos no TOTVS Educacional não fosse afetada, adicionamos na guia "Responsáveis" um grupo para cadastro de Filiação, composto por um lookup de pessoa, um flag para selecionar o tipo de relacionamento, uma grid com as filiações e os botões de manipulação da grid "Adicionar" e "Remover".  
    
 **Atenção!** O Sistema não permite que seja adicionado uma filiação com uma pessoa que já conste grid de filiações. Também não é permitido adicionar uma filiação sem informar o tipo de relacionamento selecionado.

* O Sistema não exibe como resultado do lookup de filiação a pessoa do aluno.

Para a utilização da opção "Anexo – Filiação", é necessário atribuir permissão para o usuário no módulo Educacional.   
    
 Foi criado o botão "Cadastrar PAI/MÃE como responsável" para atribuição de responsável financeiro. Ao clicar no botão, é exibida uma tela para seleção do responsável financeiro do aluno entre os pais e mães previamente cadastrados. Após a seleção, o pai ou mãe selecionado é exibido no campo logo abaixo.  
    
 Caso o aluno tenha somente uma pessoa cadastrada na seção "Filiação" o sistema exibe uma nova janela, onde é possível selecionar registro de cliente / fornecedor gerado clicando no botão "Aproveitar". Clicando em novo, é gerado um novo registro de cliente fornecedor para a pessoa cadastrada como pai ou mãe do aluno.  
    
 Na tela de atualização de endereço consta uma lista com todas as pessoas da filiação do aluno, além dos responsáveis financeiro e acadêmico.

 Veja Também

---

[Documento técnico - Cadastro de Filiação](http://tdn.totvs.com/display/LRM/TQXUUY_DT_Cadastro_De_Filiacao)
