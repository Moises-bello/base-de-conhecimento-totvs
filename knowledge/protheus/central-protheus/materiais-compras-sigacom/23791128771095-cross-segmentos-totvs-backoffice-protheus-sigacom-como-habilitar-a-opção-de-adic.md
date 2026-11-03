---
article_id: 23791128771095
category: Materiais - Compras (SIGACOM)
content_hash: ee45d4fc6f796d458529693208e63c5785d2125d458762b9ee7bdfb1d4ca7cb0
fetched_at: '2026-06-28T22:41:15.914700+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como habilitar a opção
  de adicionar um Novo Participante no Novo Fluxo de Compras - PGCA010?
type: support-article
updated_at: '2025-10-28T19:41:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23791128771095-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-habilitar-a-op%C3%A7%C3%A3o-de-adicionar-um-Novo-Participante-no-Novo-Fluxo-de-Compras-PGCA010
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35944262023063) Tempo aproximado para leitura: **00:02:00 min****

**Dúvida**Como habilitar a opção de adicionar um Novo Participante no Novo Fluxo de Compras - PGCA010?

**Ambiente**Protheus – Compras – A partir da versão 12.1.2210

**Solução**

*Como habilitar o botão*

Para habilitar essa funcionalidade, deve ser ativado o parâmetro MV\_SELFOR = 'S' que permite o comprador adicionar novos fornecedores a uma cotação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23791128738071)

*Como incluir um Novo participante na Geração da Cotação (tela de Necessidade de Compra)*

Para incluir nessa cotação um ou mais **fornecedores participantes (não cadastrado no sistema)**, é necessário clicar no botão **Novo participante**, localizado na parte superior da tela. Nele será necessário adicionar a razão social e e-mail. É obrigatório o preenchimento da razão social para a inclusão do novo fornecedor participante, não será possível duplicar a mesma. Este fornecedor ainda não estará cadastrado oficialmente no sistema, apenas participará do processo de cotação.

![](https://tdn.totvs.com.br/download/attachments/680260500/Novo%20particiipante.gif?version=1&modificationDate=1712772453847&api=v2)

Após selecionar os fornecedores desejados e incluir os Novos participantes, deverá clicar no botão **Gerar Cotação** para concluir o processo de geração de cotação.

![](https://tdn.totvs.com.br/download/attachments/680260500/gerar%20cota%C3%A7%C3%A3o.gif?version=2&modificationDate=1712783823350&api=v2)

*Como remover um Novo participante antes de finalizar a inclusão da cotação*

**Importante: Caso tenha incluído um Novo participante indevidamente e desejar removê-lo, terá que finalizar a geração da cotação para depois desqualificá-lo.** Depois de incluir um Novo participante na geração da cotação não é possível excluí-lo da tela acima antes de gerar a cotação. Será necessário gerar a cotação, ir na Tela de Cotações no NFC, editar a cotação e clicar em Desqualificar, conforme processo abaixo.

Nesta opção, o fornecedor não será considerado para as próximas etapas, bem como terá os valores inseridos na proposta zerados. Também é possível inserir uma **justificativa ou observação**para desqualificação do fornecedor.

![](https://tdn.totvs.com.br/download/attachments/680260500/Desqualificar%20.gif?version=1&modificationDate=1712948789960&api=v2)

Quando o fornecedor for desqualificado, não será possível atualizar valores da proposta. Sendo possível apenas a **visualização**

*Como incluir um Novo participante após a criação da Cotação (tela de Edição da Cotação)*

Se o usuário desejar incorporar um **novo participante após a criação da cotação**, ele poderá fazê-lo na tela de **Edição da Cotação**, onde encontrará um botão localizado no canto superior direito com essa finalidade (Novo participante). Ao clicar nesse botão, o usuário será redirecionado para uma página onde poderá inserir as informações do novo fornecedor participante. No caso de um fornecedor já cadastrado, após inserir o código do fornecedor, os dados serão automaticamente preenchidos, como exemplificado na imagem abaixo.

**Atenção**: Quando uma cotação é gerada com **amarração de produto x fornecedor** não será possível adicionar um novo participante. 

![](https://tdn.totvs.com.br/download/attachments/680260500/novo%20participante%20cadastrado.gif?version=1&modificationDate=1712873168833&api=v2)

Para fornecedores ainda não cadastrados selecione a opção "**Não**" no campo "**Fornecedor cadastrado?**" e preencha o campo de **Razão social**

![](https://tdn.totvs.com.br/download/attachments/680260500/fornecedor%20n%C3%A3o%20cadastrado%20.gif?version=1&modificationDate=1712873555383&api=v2)

*Como analisar a cotação quando o Novo participante for o vencedor*

Caso o vencedor seja um**fornecedor participante** (não cadastrado), será exibido um alerta sobre a condição do mesmo, exigindo cadastro para a conclusão do processo**.**

**![](https://tdn.totvs.com.br/download/attachments/680260500/image-2024-4-12_18-16-5.png?version=1&modificationDate=1712956566080&api=v2)**

A tela de **cadastro de fornecedor** possui quatro abas: 

1. **Cadastrais:**Formulário para preenchimento de dados do fornecedor;
2. **Adm/fin.:**Formulário para preenchimento de dados administrativos e financeiros;
3. **Fiscais:**Formulário para preenchimento de dados fiscais;
4. **Campos obrigatórios:**Formulário para preenchimento de campos obrigatórios.
5. **Campos customizados:**Formulário para preenchimento de campos customizados.

**Campos obrigatórios** serão sinalizados com asterisco (**\***) no fim do seu nome, e somente após a obtenção dos mesmos o botão **Salvar** ficará habilitado para o cadastro do fornecedor.

Para obter alguns campos de informações do fornecedor após o preenchimento do CNPJ, é necessário a utilização do parâmetro **MV\_APIFOR** (com valor .T. ), para habilitar o preenchimento automático utilizando a TOTVS CAROL.

![](https://tdn.totvs.com.br/download/attachments/680260500/inclusao_fornece.gif?version=1&modificationDate=1741373840870&api=v2)

Importante: O cadastro do novo participante deve ser realizado **durante a análise da cotação**, **caso ele seja o fornecedor vencedor,**conforme cenário mostrado acima.

Se o cadastro for incluído diretamente pela rotina **MATA020**, o sistema **não reconhecerá a relação** entre o fornecedor e o Novo participante do processo da cotação, **não conseguindo identificar que o participante já foi cadastrado**.

Portanto, o **cadastro deve ser efetuado exclusivamente pela tela do Novo Fluxo de Compras (NFC)**, **durante a etapa de análise da cotação**, garantindo assim que o sistema estabeleça corretamente o vínculo entre o fornecedor e a cotação.

***Saiba Mais:***

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
