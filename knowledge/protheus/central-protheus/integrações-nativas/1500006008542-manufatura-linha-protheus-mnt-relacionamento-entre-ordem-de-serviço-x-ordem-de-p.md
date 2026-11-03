---
article_id: 1500006008542
category: Integrações Nativas
content_hash: b804d5e8894834d3e0d1a2f0992d8ce140f4fc47f43b3f073ff554fc4fa355a9
fetched_at: '2026-06-28T22:42:35.535627+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Relacionamento entre Ordem de Serviço x
  Ordem de Produção e Produto Manutenção
type: support-article
updated_at: '2022-02-23T18:57:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006008542-Manufatura-Linha-Protheus-MNT-Relacionamento-entre-Ordem-de-Servi%C3%A7o-x-Ordem-de-Produ%C3%A7%C3%A3o-e-Produto-Manuten%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)** Tempo aproximado para leitura: **00:02:30 min**  
**Dúvida**Qual é o relacionamento entre **Ordem de Serviço - O.S**, **Ordem de Produção - O.P** e **Produto Manutenção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Versão 12  
  
**Solução**Ao inserir uma **Ordem de Serviço** e esta envolver peça de reposição fabricada, o **Manutenção de Ativos - SIGAMNT**verifica a quantidade de estoque disponível, considerando os empenhos existentes. Caso na data da necessidade da peça de reposição não exista disponibilidade, o **SIGAMNT** implanta uma **Ordem de Produção** para o produto.   
Sempre que se implanta o **SIGAMNT** é gerado automaticamente um registro neste cadastro com o código definido no parâmetro **MV\_PRODMNT - Item de estoque para ordem de produção do SIGAMNT**. O conteúdo desse parâmetro por padrão é **MANUTENCAO**. Este produto tem como propósito vincular a **Ordem de Serviço - O.S.** com a **Ordem de Produção - O.P**. Esta **O.P.** é inserida para garantir a integridade da **O.S.** com os vínculos de **Estoque/custos** **- SIGAEST** e **Planejamento e Controle da Produção - SIGA****PCP**.  
A **Ordem de Produção** é o mecanismo que inicia o processo de fabricação do produto, relacionando todos os componentes e as etapas de fabricação determinadas pela sua estrutura. Além disso, é essencial na geração das requisições dos materiais. Esta integração se dá através do parâmetro **MV\_NGMNTPC**.    
Este relacionamento da **O.P** com o produto **MANUTENCAO**, em outras palavras, faz com que se crie um vínculo entre a **O.S** com **Solicitação de Armazém- S.A** e **Solicitação de compras - S.C**. A **O.P** é a ligação entre estas informações de **Estoque/Custos**.   
Quando da geração de **Plano de Manutenção - MNTA340**, na implantação de **Ordem de Serviço Manual - MNTA410** ou **Ordem de Serviço Corretiva - MNTA420**, o **SIGAMNT** utiliza as informações de empenhos já colocados bem como a posição de saldo de estoque para obter a disponibilidade da peça de reposição requerida. Já na confirmação do plano de manutenção e também na implantação de **Ordem de Serviço Manual** ou **Corretiva**, para cada peça de reposição necessária será implantado um empenho, conforme o *status* do parâmetro **MV\_NGMNTES - Integração com o Estoque e Custos**.  
  
**Saiba mais**Para ter acesso a documentação deste processo, acesse o *link*: [Relacionamento entre O.S x O.P e Produto Manutenção](https://tdn.totvs.com/pages/releaseview.action?pageId=567750522).
