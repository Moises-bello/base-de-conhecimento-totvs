---
content_hash: 9673a81f1af6189cbff0f7f40631259c2bcf70d952bb7d2ea0c79d6e00026900
fetched_at: '2026-06-29T00:09:18.150784+00:00'
page_id: '421388689'
product: rm
source: tdn-rm
title: Template de Acordo
type: documentation
url: https://tdn.totvs.com/display/LRM/Template+de+Acordo
version: 14
---

O Template de Acordo foi desenvolvido com o objetivo de permitir a definição de layouts que estarão visíveis ao usuário, sendo possível escolher o melhor plano de pagamento baseado nos valores dos lançamentos Financeiros. A parametrização de recursos como Juros simples, Juros compostos, Valores / Percentual a Acrescentar, Valores / Percentual a Descontar entre outros devem ser realizados neste processo.

As regras do Template valem apenas para o momento que o acordo está sendo gerado, e podem ser alteradas posteriormente. É o que ocorre, por exemplo, com os parâmetros do Financeiro, podem ser alterados mesmo que já existam lançamentos gerados.

Nas bases convertidas para versão cuja funcionalidade foi liberada será criado automaticamente um Template que será utilizado de forma mais abrangente, pois no processo antigo de Acordo não existia as novas restrições. Caso seja de interesse alterar as permissões o usuário deve editar o Template criado na conversão e parametrizar com as regras de acordo desejadas.  
Para iniciar a utilização certifique através do Perfil de Usuário em Serviços Globais as permissões para (Incluir |Editar | Aprovar e Excluir).  
A opção do Template de Acordo está disponível no Menu: Contas a Pagar - Receber | Operações | Acordo | Template de Acordo. É obrigatório o vínculo de pelo menos um Template de Acordo vinculado ao perfil de usuário que estará utilizando o  Módulo de Acordo.

Caso não exista associação ao iniciar o assistente de acordo será apresentada a seguinte mensagem: "Perfis associados ao usuário não possui Templates de Acordo vinculados."   
Para os templates indicados os usuários ligados ao perfil terão permissão de selecionar o template como modelo no processo de geração de Acordos. A tabela que vincula o perfil ao template de acordo é a FTEMPLATEACORDOPEFIL. Um registro de Template de Acordo pode ser vinculado a mais de um perfil, ao mesmo perfil podem estar vinculados vários registros de Template de Acordo e o cadastro é feito por coligada.  
Para que seja efetivo a liberação ou restrição de acesso é necessário realizar Logout | Login após alterações no perfil de usuários. Será possível definir regras de interface individuais para cada Template de Acordo conforme as opções abaixo:

**Observações:**

Após definição dos dados e permissões do Template o mesmo será gerado e poderá ser utilizado nas negociações dos Lançamentos Financeiros através da Visão de Lançamentos ou através da Negociação Online.

**Anexos**

[Matriz Aplicada](https://tdn.totvs.com/x/dPtbGQ) - possibilita vincular qualquer Template de Acordo à Matriz Aplicada do Módulo Educacional.

Essa opção somente será apresentada caso haja integração entre os módulos: Totvs Educacional e o Totvs Gestão Financeira e ser verificado no Menu: Ambiente | Parâmetros | Integrações de Sistemas. É necessário informar a matriz aplicada pelos campos Curso, Habilitação, Matriz Curricular e Turno. Este vinculo será realizado com o intuito de integrar o Template ao Portal do Educacional, para o Totvs Gestão Financeira o vínculo deste não interfere nas negociações realizadas pela Visão de Lançamentos. No contexto do Totvs Gestão Financeira será preciso verificar o nível de ensino do Educacional, para que a Matriz Aplicada seja apresentada corretamente.

[Serviço](https://tdn.totvs.com/x/wPxbGQ) - possibilita vincular qualquer “Template de Acordo” a um ou vários serviços do Totvs Educacional. Basta criar um novo e informar o código do serviço. Essa vinculação facilitará e permitirá controlar os modelos de acordo por tipo de serviço de contrato do Educacional, garantindo mais flexibilidade para direcionar a negociação para o modelo mais compatível.

Ao gerar um acordo serão buscados todos os templates vinculados ao serviço, e caso não existam nenhum, trará todos que atendam as demais regras de seleção existentes para o template.

Importante: no Portal Educacional caso não exista template vinculado ao serviço o processo de negociação é barrado.

**Usabilidade**

Quando o (s) lançamento (s) de origem do acordo for do Educacional, no processo de geração de acordo somente os templates com o serviço correspondente vinculado serão apresentados para seleção. Caso exista mais de um template vinculados ao mesmo serviço, todos serão exibidos, desde que atendam as demais regras de seleção do processo de negociação.

Quando no serviço nenhum template estiver vinculado, ao gerar o acordo todos os templates já existentes do processo de negociação serão apresentados para seleção.

Para acordos cujos lançamentos de origem não for do Educacional essa regra não será aplicada.

Tabelas envolvidas:

* FLAN
* SLAN
* SPARCELA
* SSERVICO
* STEMPLATEACORDOSERVICO
