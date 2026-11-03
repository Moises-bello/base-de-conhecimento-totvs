---
content_hash: 9b0dc529b0be7de7fd7a85a6b60ec2441374dd115000dcad70e4aa6fd285672d
fetched_at: '2026-06-29T00:11:10.159772+00:00'
page_id: '641678463'
product: rm
source: tdn-rm
title: Pré-Venda - Alçadas de Aprovação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=641678463
version: 4
---

### **Definição:**

---

A "alçada de aprovação" é um processo que estabelece os níveis de autorização e aprovação necessários para concessões de desconto ou aprovações em propostas de empreendimentos.   
Ela determina quais grupos de usuários têm permissão para conceder descontos e em que medida, com base em um percentual do Valor Líquido de Proposta (% VLP). Geralmente, envolve uma aprovação dupla, com diferentes usuários, para ser ativada. A alçada de aprovação controla e gerencia as decisões de aprovação e desconto em transações comerciais.

**Pré-requisitos:**

---

Existem alguns pré requisitos a serem parametrizados no sistema para que possa ser configurado uma alçada de aprovação:

* Supervisor: é necessário possuir no grupo de usuários as permissões marcadas: "Autorizar proposta Reprovada" e "Alterar sitiuação da proposta";
* Corretor: para que o mesmo possa solicitar aprovação, é necessário desmarcar no grupo de usuários a opção de: "Autorizar proposta Reprovada" e "Alterar situação da proposta".

**Parametrização no sistema:**

---

Para realizar a parametrização de uma alçada de aprovação acesse no portal de Imóveis o Frontent > Pré-venda > Alçadas de aprovação.

Nesta visão será possível consultar, editar, incluir ou excluir uma alçada de aprovação. Para realizar a inclusão de uma nova alçada será apresentado no menu superior direto um botão Adicionar:

Na inserção de uma nova alçada alguns campos serão de preenchimento obrigatório:

**Inicio:** Data de inicio de validade dessa alçada.  
**Fim:**Data de fim de validade dessa alçada.  
**VPL de Aprovação:** será listado todos os grupos cadastrados permitindo informar um % para cada grupo.  
**Empreendimento:** Deve ser selecionar um Empreendimento para a alçada, após selecionar o empreendimento será listados todas as subunidade do empreendimento permitindo a sua seleção.

O percentual de VPL padrão (nativo) para todos os empreendimentos e grupos já vem com o percentual de 100%, portanto, (como um exemplo) caso um grupo possa realizar 2% de desconto, o percentual da taxa de aprovação que este deverá ser alterada para 98%.

* O sistema segue uma ordem que é validada para buscar a porcentagem de desconto aceito em uma unidade do empreendimento em proposta.  
  0 - Sistema inicia o percentual VPL esperando que seja 100% (Caso não exista Alçada de Aprovação para o Empreendimento/unidade)  
  1 - Unidade promoção por grupo usuário (Alçada de aprovação)  
  2 - Modalidade Taxa VPL (caso haja modalidade principal do empreendimento e a taxa VPL for maior que 0)  
  3 - Empreendimento percentual VPL aprovação.
* Caso já exista alguma alçada cadastrada, é importante realizar uma conferencia dos % para os grupos de usuário.

Ao final desta inclusão a situação do registro ficará "Aguardando aprovação" sendo necessário se acesado a opção aprovar (por dois supervisores para que esta situação fique com o status ATIVA e possa ser utilizadas nas alçadas (do empreendimento parametrizado), observe no exemplo abaixo 2 registros existentes, onde um encontra-se ATIVO e o outro inativo.

Após a aprovação dupla (realizada por diferentes usuários), a alçada estará ativa e pronta para ser aplicada em novas propostas. Se for necessário efetuar alguma modificação na alçada, será imprescindível obter uma nova aprovação para que as alterações se tornem ativas novamente.

**Exemplo de utilização:**

---

No cadastro da Alçada de Aprovação, foi especificado que os usuários associados ao grupo "Administrador" têm um percentual de VPL de 98%.

Com essa configuração usuários vinculados ao grupo Administrador ao realizar uma proposta para uma subunidade que possui essa alçada de aprovação poderão conceder um desconto de até 2%, visto que o valor mínimo de VPL é 98% para este grupo de usuário. Caso o usuário tente informar um desconto maior que 2% ao tentar validar as condições de pagamento da proposta será apresentado uma mensagem informando que a proposta não foi aprovada. 

Para obter mais informações sobre a Alçada de Aprovação e seu processo de aprovação via e-mail, acesse:  [Envio de email - Alçada de aprovação - Nova proposta](https://tdn.totvs.com/pages/viewpage.action?pageId=759938600)
