---
article_id: 360022000471
category: SIGAEST - RELATORIOS
content_hash: 1b7055bba807e97f633633cf710f03da131fb7bb0cd4eeece3fbed9acb76ae9c
fetched_at: '2026-06-28T22:39:05.988547+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Relatório Posição
  de Estoque (MATR260) não traz registros
type: support-article
updated_at: '2022-08-08T12:11:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022000471-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Relat%C3%B3rio-Posi%C3%A7%C3%A3o-de-Estoque-MATR260-n%C3%A3o-traz-registros
---

**Dúvida**Gerando o relatório MATR260 não traz nenhum registro, independente da parametrização informada; Como encontrar o problema?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Este problema ocorre na maioria das vezes devido a alteração de dicionário ou registros da base, compartilhamento de tabelas ou falta de registros complementares (como armazém).

**1.** **Premissa inicial para avaliação do** **problema**- Mantenha sempre o pacote acumulado do módulo de Estoque/Custos atualizado.

***Pacotes acumulados Estoque/Custos:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571) **|** 12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640) **|** 12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/748747)

OBS: Sempre atualizar primeiramente em ambiente de homologação.

**2.** Com a acumulado do Estoque/Custos atualizado, geramos o relatório MATR260 parametrizando todas as perguntas para **"****de '     ' a 'ZZZZZZZZZ'****".** Selecionamos também o **"Saldo do Produto à Considerar = Saldo Atual"**.

**3.** Acessamos o DBMonitor e localizamos o usuário que está gerando o relatório, selecionamos a opção **Rastrear**, será aberto uma tela com o relatório sendo rastreado. Após gerarmos o relatório e verificarmos o arquivo que foi gerado, procure por **GETQUERYFILE (**ali estará a query que o relatório utiliza para geração dos arquivos). Copie esta Query e cole no seu Banco de Dados. Posteriormente, verifique todos os campos que a query utilizou, localizando o campo que está incorreto, verifique o motivo do erro e ajuste se necessário.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Relatórios no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)*
