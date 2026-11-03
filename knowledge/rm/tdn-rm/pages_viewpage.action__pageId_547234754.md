---
content_hash: e4e63532fc4a47ceef98b1eb763d7e53a1776345bc0237c7fb83ce98e475f756
fetched_at: '2026-06-29T00:10:42.276913+00:00'
page_id: '547234754'
product: rm
source: tdn-rm
title: RM - FOP - MP 932/2020 - Redução da contribuição ao sistema “S” - Preenchimento
  Global
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547234754
version: 10
---

Conforme a publicação da MP n° 932/2020, o  objetivo é diminuir os custos para o empregador em meio à crise causada pelo novo coronavírus. Ela possibilita a redução pela metade da contribuição obrigatória das empresas ao Sistema “S” por 3 meses.

Orientamos através da [FAQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045623814-RM-FOP-MP-932-2020-Redu%C3%A7%C3%A3o-da-contribui%C3%A7%C3%A3o-ao-sistema-S-) disponibilizada pela nossa central de atendimento, para que na geração das rotinas Guia de INSS e Folha Analítica considere o percentual reduzido, poderá ser feito a alteração do campo % Terceiros individual em cada seção.

Também disponibilizamos no cadastro de Seção o 'Histórico de Percentual para INSS' para que seja inserido o percentual do INSS Patronal, Terceiros e Acidente de Trabalho que será considerada conforme a competência informada. Assim para estas competências cadastradas, nas rotinas acima irão considerar o histórico e não a alíquota está no cadastro da Seção nos campos %Terceiros e %Acid. Trabalho, assim como o %Empresa informado em ambas rotinas. 

O passo a passo para acessar este recurso, como fazer o preenchimento de forma individual e o resultado nas rotinas de Folha Analítica e Guia de INSS está documentado no [Histórico de Percentuais para INSS](https://tdn.totvs.com.br/pages/releaseview.action?pageId=496388652).

**Preenchimento Global**

falseImportante

**Os recurso de Alteração Global dos Dados de INSS da Seção estará disponível a partir dos patchs abaixo:**

* **12.1.25.271**
* **12.1.26.217**
* **12.1.27.173**
* **12.1.28.107**

Disponibilizamos o recurso para preenchimento Global deste cadastro, localizado em Administração de Pessoal | Alterações Globais | Alterações de Cadastro | Alterações de Dados do INSS da Seção. Por este processo é possível incluir, alterar ou remover o histórico de dados do INSS da seção conforme as parametrizações gerais e/ou específicas.

falseImportante

* Este processo é habilitado somente se o parâmetro "Habilita Histórico de INSS no Cadastro de Seção (Produtor Rural)" tiver sido marcado no parametrizador em Folha Normal | Encargos Sociais. Como o processo é multi-coligada, as coligadas devem ter o parâmetro habilitado para que seja executado com sucesso.
* Para acessar esta funcionalidade é necessário também habilitar o item de menu 01.03.01.10 Alteração Dados INSS da Seção em Globais no Cadastros dos Perfis.

*Inclusão*

Na inclusão, deve ser informado a competência inicial e final e os percentuais que serão  considerados para a geração da Guia de INSS e Folha Analítica. Ao avançar a interface que preenche os percentuais e vigência, será possível selecionar as coligadas que devem inserir os dados do Histórico de INSS.

 

Após a conclusão do processo é apresentadas no log as seções que foram inserido os dados:

No Histórico de percentual para INSS o registro foi gravado.

*Alteração*

Para alteração o processo valida a competência inicial informada e caso exista algum registro com a mesma competência, os dados serão atualizados. No exemplo abaixo foram alteradas as alíquotas % empresa e % Acid. Trabalho e a data fim da vigência. No final do processo, retorna o log com as seções alteradas:

 

No histórico de percentual para INSS o registro foi alterado:

*Exclusão*

Para exclusão, foi disponibilizado a flag 'Remover', que quando marcada, assim como na alteração valida a competência inicial informada e caso exista algum registro com a mesma competência, os dados serão removidos.

No exemplo abaixo, selecionei a seção 01, e marquei para remover. NO log retornou a seção que teve o registro removido:

  

No cadastro do Histórico de percentual para INSS o registro foi apagado:

falseAtenção

* Somente será considerada a seção centralizadora da coligada estando de acordo com a quebra de CNPJ parametrizada no Parametrizador | RH – Máscaras e Quebras.
* Caso exista o histórico e o percentual for 0 (Zero) o mesmo será considerado para a geração da Guia de INSS e Folha Analítica, logo é necessário preencher os três campo para o correto cálculo dos encargos.
* Caso o registro esteja fora da vigência será considerado o valor cadastrado na seção e informado nas interfaces dos processos (para % Empresa).
* O preenchimento Global só altera este histórico não persistindo os percentuais no Cadastro de Seção aba 'Dados para INSS'.
