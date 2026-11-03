---
article_id: 31153172997015
category: SIGAEST - CUSTOS
content_hash: fb4159216b639a662eaaade9e39a437eb7de9eb18b6aad83ad5d49974e13495c
fetched_at: '2026-06-28T22:39:00.877746+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Dados para abertura
  de tickets de Custos agilizar o atendimento
type: support-article
updated_at: '2026-06-11T20:19:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31153172997015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Dados-para-abertura-de-tickets-de-Custos-agilizar-o-atendimento
---

Para abrir um ticket no módulo de Custos do TOTVS Protheus SIGAEST com agilidade, envie diagnóstico do sistema pela Central de Diagnóstico, confirme as Stored Procedures atualizadas, envie dados de processamento (tabelas D3X ou CV8), relatórios Kardex (MATR900) em PDF, detalhamento de OP (PCPR860) em planilha, informe método de custeio MOD/GGF, tabela temporária TRB em SQLITE e evidencie customizações ativas.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31153189062295) Tempo aproximado para leitura: **00:02:45 min**

**Dúvida**

Quais informações e arquivos devem ser enviados na abertura de um ticket relacionado ao módulo de Custos para garantir agilidade e assertividade na análise técnica?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões

**Solução**

Os incidentes e dúvidas relacionados ao processamento de Custos possuem alta complexidade, pois dependem da análise de diversos parâmetros, configurações e integridade de dados. Para que o suporte técnico possa realizar o diagnóstico de forma eficiente, é indispensável o envio de um conjunto de informações padronizadas.

**Os arquivos LOGS contidos CV8,D3X,D3Y,D3W não são arquivos contidos dados sensiveis**, a extração pode ser feita e encaminhada ao time de suporte para avaliação dos log e campos MEMO.

1. **Diagnóstico do Sistema:** Gere e envie os dados da [**Central de Diagnóstico**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico). Esse recurso consolida informações críticas do ambiente para análise remota.
2. **Stored Procedures:** Confirme se as [**Stored Procedures**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel) de Custos estão instaladas e atualizadas na versão correta.
3. **Dados de Processamento:** Se a ocorrência envolver a avaliação dos custos no Kardex, certifique-se que a rotina Acompanha Custos ou Custo medio, ja tenha sido processadas, e então, envie as tabelas **D3X(Se feito no MATA038),CV8(Se feito no MATA330)** em formato SQLITE filtradas pela data do processamento.
4. **Relatórios de Conferência:**

   * **Kardex (MATR900):** Envie em PDF, incluindo obrigatoriamente a página de parâmetros, sempre, sempre parametrizar como orienta o boletim: [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es)(MATR900)- [SmartView](https://tdn.totvs.com/display/PROT/Smart+View+-+Kardex)
   * **Detalhamento de OP:** Para casos envolvendo Ordens de Produção, envie em formato de planilha, também com a página de parâmetros o SmartView [PCPR860](https://tdn.totvs.com/pages/viewpage.action?pageId=777935258)
5. **Mão de Obra (MOD):** Se sua duvida, é sobre o custo do MOD ou GGF, sempre fnforme se o método utilizado para o custeio de MOD e GGF é **Com Integração Contábil** ou **Sem Integração Contábil**.

   Valide aqui as diferenças dos valores em cada tipo pra entender melhor: [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402062082071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-de-configura%C3%A7%C3%A3o-de-MOD-e-GGF-Sem-e-Com-integra%C3%A7%C3%A3o-cont%C3%A1bil)
6. **Tabela Temporária TRB:** Se o erro persistir após o Custo Médio, gere e envie a tabela temporária **TRB** em formato SQLITE (.sdb) seguindo o procedimento do boletim, para gerar o arquivo filtrado pelo produto, ele é extremamente importante para que possamos avaliar a ordenação dos movimentos e então validar se esta de acordo Kadex e parametros contidos nos arquivos D3X ou CV8, [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011904591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-extrair-arquivo-de-trabalho-TRB-ao-executar-o-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-MATA330)
7. **Evidências e Customizações:**

   * Informe se existem **Pontos de Entrada (Customizações)** ativos. Recomenda-se realizar um teste com as customizações desabilitadas antes do envio do ticket.

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[COMO GERAR O TICKET PARA TER UM ATENDIMENTO MAIS ÁGIL E ASSERTIVO](https://tdn.totvs.com/x/mrcYIQ)

[MATR900 - Como configurar corretamente o relatório Kardex para análise de Custos e Movimentações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es)

[MATR900 - Interpretando o Custo no Kardex antes e depois do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005781102-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Interpretando-o-Custo-no-Kardex-antes-e-depois-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)

[SIGAEST - MATR860 - Interpretando Custos em Ordem de Produção (OP)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012330641-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR860-Interpretando-Custos-em-Ordem-de-Produ%C3%A7%C3%A3o-OP)

[SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel)

[SIGAEST - Processo de configuração de MOD e GGF "Sem" e "Com" integração contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402062082071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-de-configura%C3%A7%C3%A3o-de-MOD-e-GGF-Sem-e-Com-integra%C3%A7%C3%A3o-cont%C3%A1bil)

[SIGAEST - MATA330 - Como extrair o arquivo TRB após executar o custo medio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011904591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-extrair-o-arquivo-TRB-ap%C3%B3s-executar-o-custo-medio)

[SIGAEST - Como é feita a ordenação dos movimentos após recálculo do custo médio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17221653862551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-feita-a-ordena%C3%A7%C3%A3o-dos-movimentos-ap%C3%B3s-rec%C3%A1lculo-do-custo-m%C3%A9dio)
