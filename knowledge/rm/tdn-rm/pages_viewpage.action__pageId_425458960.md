---
content_hash: 328fa27bab8d6ffbd270c3ca68c049e9c489e6b5a21eb856c1278e8c0b9d15a5
fetched_at: '2026-06-29T00:09:33.298064+00:00'
page_id: '425458960'
product: rm
source: tdn-rm
title: Integração com Totvs Gestão de Estoques, Compras e Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458960
version: 3
---

**Integração com Totvs Gestão de Estoques, Compras e Faturamento**

---

O TOTVS Aprovações e Atendimento integra com o Totvs Gestão de Estoques, Compras e Faturamente para aprovação de movimentos, cotações, etc por fluxo de trabalho.

**Desenvolvimento/Procedimento**   
1.      Criar um tipo de atendimento.   
Acesse: Cadastros / Atendimentos / Tipos de atendimentos / Inlcuir  
Preencha os campos necessários e clique em SALVAR, para criar o tipo de atendimento.  
2.      Criar uma etapa e indicar que será a primeira etapa de um possível fluxo.   
3.      Criar um grupo de atendimento e vincular o tipo de atendimento criado a esse grupo.  
4.      Acessar o Nucleus e parametrizar o tipo de movimento desejado com as informações de integração necessária. Clique em OPÇÕES | PARAMETROS | RM NUCLEUS | ESCOLHA O TIPO DE MOVIMENTO DESEJADO E CLIQUE EM EDITAR, conforme prints abaixo:  
5.      O movimento é criado no Nucleus e fica em aprovação por workflow e é criado, também, no Agilis um atendimento para que seja executado o fluxo de trabalho até a aprovação final. O movimento só é liberado quando o atendimento é concluído confirmado ou cancelado. Perceba que o atendimento é criado na 1ª etapa do tipo de atendimento e a solicitação do mesmo contém alguns dados padrões referente ao movimento do Nucleus.

**Descrição do Processo**  
 A integração entre o Nucleus e o TOTVS Aprovações e Atendimento consiste em ter uma aprovação de movimentos, cotações por fluxo de trabalho. No momento que o movimento está sendo criado, um atendimento é inserido no TOTVS Aprovações e Atendimento, e até que o mesmo seja concluído ou cancelado, o movimento não estará liberado para faturamento, por exemplo.  
Confira o passo a passo, juntamente com as telas no nosso blog.

**Recursos Adicionais**

[Blog - Integração Totvs Gestão de Pessoas](http://totvsconnect.blogspot.com/2010/11/integracao-com-o-totvs-gestao-de)
