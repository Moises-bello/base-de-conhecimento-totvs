---
content_hash: ebe55d75630c4ab9603099378e75114b4a39350deda881212676a04bdc34eadb
fetched_at: '2026-06-29T00:10:08.846491+00:00'
page_id: '452719593'
product: rm
source: tdn-rm
title: Folha de Pagamento - Lotação Tributária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719593
version: 11
---

Lotação tem o conceito estritamente tributário e não físico e influi no método de cálculo da contribuição previdenciária para um grupo de segurados específicos, não refletindo, necessariamente, o local de trabalho do empregado. Identifica a classificação da atividade para fins de atribuição do código FPAS, a obra de construção civil, o contratante de serviço, ou uma condição diferenciada de tributação. A condição diferenciada ocorre quando uma determinada unidade da empresa possui um código de FPAS/Outras Entidades e Fundos distintos.   
   
   
Para as empresas que não utilizam tomadores de serviços   
Serão consideradas como lotações tributárias as seções centralizadoras de CNPJ, e as seções centralizadores de FPAS (empresas que possuem mais de um FPAS dentro de um mesmo CNPJ).  
   
**Atenção:**  
Nesta tela será exibida uma visão com as seções centralizadoras de CNPJ e de FPAS.  
   
Não permitirá inclusões, alterações ou exclusões, visto que os dados serão obtidos à partir do cadastro de seções.  
   
O duplo click em uma linha da visão acessará o cadastro da seção, permitindo alterações na seção de acordo com as permissões do usuário.  
   
   
   
Para as empresas que utilizam tomadores de serviços  
Serão consideradas como lotações tributárias os tomadores (Clientes/Fornecedores) que tiverem o campo "Tomador de serviço folha" marcado.  
   
Será necessário o preenchimento das informações abaixo:

**Código Lotação:** Código gerado automaticamente conforme máscara definida no parametrizador.  
   
**Tipo de Lotação:** Serão listados os tipos de lotações referente aos tomadores de serviço, conforme manual no eSocial.

**Empreitada Parcial onde o Tomador é o proprietário da obra:** Habilita somente quando o **Tipo da Lotação** for igual a **02**. E é utilizado para geração do evento S-1020 no e-Social.

**Seção:** Serão listadas as seções centralizadoras e de quebra de FPAS (somente as seções que tiverem o campo FPAS preenchido).  
   
**Código Tomador:** *S*erão listados os registros do cadastro de Cliente/Fornecedor ativos e que possuem o campo "Tomador de serviço Folha" marcado.  
   
**CEI:** *S*erão listados os números de CEI associados ao Tomador informado no registro anterior.  
   
**Considera dados da seção:** Marcando esse campo serão considerados os campos: FPAS, Código de Terceiro e Código Suspenso de terceiro da Seção escolhida acima.  
**Atenção:** Com este campo desmarcado o FPAS e Código de Terceiros se tornam obrigatórios*.*  
   
**Código suspenso de terceiros:** Preenchendo este campo a informação de Processos Judiciais no anexo desse cadastro se torna obrigatória.  
**Atenção:** Para as coligadas que utilizam tomador de serviço, este cadastro será alimentado sempre que for executado o processo ["Gerar Lotação Tributária"](http://tdn.totvs.com/pages/viewpage.action?pageId=452719444), quando inserir um registro no rateio de tomadores no cadastro do funcionário, quando efetuar entrada de movimento por tomador ou quando informar um tomador no histórico de afastamento do funcionário. Nesses casos a Lotação Tributária será criada caso ainda não exista.  
   
**Observação:** Ao Utilizar Tomadores de Serviços, será necessário executar o processo ["Gerar Lotação Tributária"](http://tdn.totvs.com/pages/viewpage.action?pageId=452719444) antes de ["Gerar Gatilhos Eventos Iniciais"](http://tdn.totvs.com/pages/viewpage.action?pageId=452719489).

O campo '**Empreitada Parcial'** precisa do script "**LB.2019.01\_06**"para as versões anteriores a 12.1.24, disponível na central de downloads.  
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Processo Judicial de Terceiros   
Gerar Lotação Tributária
