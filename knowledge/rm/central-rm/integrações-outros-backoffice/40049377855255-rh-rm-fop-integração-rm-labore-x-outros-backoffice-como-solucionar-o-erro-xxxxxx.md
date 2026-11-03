---
article_id: 40049377855255
category: Integrações Outros BackOffice
content_hash: b50c07ebd1b70a3eb75a762cf177bad437566afbdc43f4e71b4102b90a7caef6
fetched_at: '2026-06-28T22:46:42.065522+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RH - RM - FOP - Integração RM Labore x Outros BackOffice - Como solucionar
  o erro "xxxxxxxx' não integrado?
type: support-article
updated_at: '2026-04-29T16:17:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40049377855255-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-Outros-BackOffice-Como-solucionar-o-erro-xxxxxxxx-n%C3%A3o-integrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40049416007191) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como solucionar o erro de algum registro "xxxxxxxx' não integrado?  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40049377831703)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Quando é realizada a integração do RM com outros sistemas de backoffice, como Protheus ou TOTVS Moda, pode ocorrer o erro informando que determinado registro “XXXXXX não integrado”.

Esse tipo de erro pode estar relacionado a diversos cadastros compartilhados entre os sistemas, como:

* Conta contábil (débito/crédito)
* Classe de valor
* Item contábil
* Centro de custos
* Natureza financeira
* Fornecedores
* Função
* Seção
* Outros

De forma geral, esse erro indica que o registro em questão não possui o vínculo de integração (DE/PARA) devidamente configurado. Ou seja, o sistema não consegue identificar a correspondência entre a coligada e o registro no RM com o respectivo grupo de empresa, filial ou cadastro no outro sistema (Protheus ou TOTVS Moda).

Vale destacar que o escopo da integração é garantir a sincronização dos cadastros de backoffice entre os sistemas envolvidos. Portanto, para que a integração funcione corretamente, é indispensável que todos os registros estejam previamente mapeados por meio do DE/PARA.

Escopo da integração [**RM x TOTVS Moda**](https://tdn.totvs.com/pages/releaseview.action?pageId=602635497)

Escopo da integração [**RM x Protheus**](https://tdn.totvs.com/display/public/INT/Manual_Doc_Integracao_RMLabore_BackOfficeProtheus)

**Correção**

Acesse o sistema responsável pelo envio do registro que apresentou o erro “Não integrado”, após validar se ele faz parte do escopo da integração.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40049377833623)

Em seguida, realize uma pequena alteração no cadastro, como, por exemplo, na descrição do item, e salve. Essa ação força o reenvio do registro, permitindo que a integração ocorra corretamente entre os sistemas e que o DE/PARA seja criado automaticamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40049377834903)

No exemplo citado, a “Classe de Valor 5 não integrada” foi corrigida após a edição de sua descrição. Com isso, o registro foi reenviado ao RM e o vínculo (DE/PARA) foi criado com sucesso.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40049377835671)

Seguindo esse mesmo princípio, para qualquer item que apresente erro de “não integrado”, basta acessar o sistema de origem e:

* editar alguma informação do cadastro para forçar o reenvio, ou
* executar uma [**carga de dados**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20973528875543-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-EAI-Carga-de-Dados) (quando aplicável), garantindo que o adapter envie novamente as informações.

Essas ações permitem que o vínculo entre os sistemas seja estabelecido corretamente, eliminando o erro na integração.

Se o erro persistir, acesse **Integração | EAI 2.0 | De/Para** e valide se o vínculo foi criado corretamente, conferindo coligada, empresa/filial e possíveis inconsistências ou duplicidades.

Caso identifique problemas, ajuste o DE/PARA existente ou exclua-o para que seja recriado automaticamente no próximo reenvio do cadastro, garantindo a consistência das informações e a resolução do erro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40049377836823)
