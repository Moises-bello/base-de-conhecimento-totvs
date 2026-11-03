---
article_id: 360024707733
category: Meu RH - Pagamento
content_hash: aa1168ff9bb1d07690133a1816ebee15714290110ea6c3cf8da25269d12014f0
fetched_at: '2026-06-28T22:47:33.903395+00:00'
product: rm
section_id: 1500000835221
source: central-rm
title: RH - RM - Meu RH - Como configurar e visualizar o Informe de rendimentos no
  app Meu RH
type: support-article
updated_at: '2026-03-04T17:58:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024707733-RH-RM-Meu-RH-Como-configurar-e-visualizar-o-Informe-de-rendimentos-no-app-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22216290612119) Tempo aproximado para leitura: 00:02:56 min**

**Dúvida**  
Quando o Informe de Rendimentos não é apresentado, como proceder?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.27  
  
**Solução**  
Foi criado um passo a passo com todas as configurações necessárias para disponibilizar o Informe de Rendimentos via Meu RH, favor conferir detalhadamente:  
  
**Passo 1:** Conferir se o Perfil vinculado aos usuários dos funcionários, estão com a permissão correta, deverá permitir o menu abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12073912184599)  
  
**Passo 2:** Acessar a **Folha de Pagamento / Configurações / Parametrizador / RM Portal - Edite o Quiosque vinculado aos funcionários** e clique em **Informe de Rendimentos**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12073801328023)

Parâmetro **Gera Informe via Gerador de Relatórios**, recomendamos que deixe o parâmetro **desmarcado**, pois será gerado o Informe de Rendimentos interno e padrão TOTVS, a flag somente deverá ser marcada quando o próprio Cliente for "customizar" o Informe de Rendimentos.  
Informe o ano dos Informe de Rendimentos que deseja liberar no Portal e Meu RH.  
  
**Observação:**Esse período será respeitado de acordo com as informações gravadas na tabela PDIRF.  
  
**Passo 3:** Aparecerá o Informe de Rendimentos no Meu RH, somente se a tabela **PDIRF** estiver alimentada corretamente para os funcionários, para alimentar essa tabela com os dados do Informe de Rendimentos, deverá realizar os procedimentos abaixo:  
  
**3.1** Acessar: **Anuais / Dirf/Informe de Rendimentos** e selecione a opção **Informe de Rendimentos**:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12073956207255)  
  
**3.2** Avance, clique em **"Adicionar Parâmetros a Coligada"**.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12074009914519)

Confira se foi configurado corretamente a Seleção de Funcionário, com os funcionários que deseja alimentar a tabela PDIRF:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12074008037783)  
  
**3.3** Clique em "Informe de Rendimentos" e marque os parâmetros conforme sugestão do print abaixo:

**OBSERVAÇÃO:**A flag "Deletar Ano de Referência" deverá ser marcada caso for alimentar a PDIRF para todos os funcionários pois ela tem a função de limpar os dados dessa tabela referentes ao ano base selecionado. Portanto, caso for gerar somente para um funcionário por exemplo, **não deverá ser marcado** a flag: "Deletar Ano de Referência".  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12074063143447)  
  
**3.4** Clique em Ok e avança para a geração ! Após finalizar a geração da rotina, poderá realizar a consulta abaixo no Banco de Dados, para comprovar se a tabela PDIRF foi alimentada, segue um exemplo:  
  
SELECT \* FROM PDIRF WHERE CHAPA='XXXX' onde 'XXXX' é a chapa do funcionário  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003007362)  
  
Conforme exemplo do print acima, vemos que foi alimentado os dados do Informe de Rendimentos do ano 2020 para a Chapa 00002, portanto, se todos os passos anteriores estiverem corretos, ao Logar no Meu RH, aparecerá o informe de rendimentos de 2020:  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104052813)  
  
**Passo 4:** Para visualização do Informe de Rendimentos é necessário que o usuário tenha instalado um aplicativo visualizador de **PDF** no seu *smartphone*. O informe é gerado em arquivo formato pdf.

O informe de rendimento terá opções de Download e Compartilhamento conforme a tabela.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22216259621527)  
  
Para mais informações detalhadas [Clique Aqui.](https://tdn.totvs.com/display/NPR/7.0+Informe+de+Rendimentos)  
  
**Observação:**Caso o funcionário tenha transferência de Coligada ou Filial no ano posterior, o Informe de Rendimentos poderá ser visualizado exclusivamente pela Chapa de origem (Chapa demitida). Via Meu RH  basta o usuário alterar o Contexto para visualizar a Chapa demitida.
