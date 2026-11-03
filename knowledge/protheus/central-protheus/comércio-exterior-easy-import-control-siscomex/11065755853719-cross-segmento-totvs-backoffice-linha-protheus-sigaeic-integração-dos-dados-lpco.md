---
article_id: 11065755853719
category: Comércio Exterior - Easy Import Control - Siscomex
content_hash: 7c9e7d042c9dca40809926228bc31d2b6f6b0fcce7604a749e2ee232039e1c5c
fetched_at: '2026-06-28T22:39:45.287753+00:00'
product: protheus
section_id: 1500001538441
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Integração dos
  dados LPCO
type: support-article
updated_at: '2022-12-19T18:34:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11065755853719-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Integra%C3%A7%C3%A3o-dos-dados-LPCO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como efetuar integração dos dados (LPCO)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  –*Easy Import Control*– a partir da versão 12.1.27  
  
**Solução**Para disparar a integração dos dados dos registros marcados para o portal único Siscomex.  
**Restrições:**           - Só são exibidos os registros com status "**integrado?**" = **Não**.

1. No módulo **SIGAEIC** ou **SIGAEEC**, acessar o Menu **Atualizações\Portal Unico\Integração LPCO**.
2. Verificar que os registros virão filtrados conforme a visão default do módulo, ou seja, modalidade "**1-Importação**" se **SIGAEIC** e modalidade "**2-Exportação**" se **SIGAEEC**.
3. Clique na guia de visões padrão do browser ( á direita do título da tela na parte superior) e altere para a visão de preferência.
4. Marcar os registros que serão integrados para o Portal Único.
5. Clicar no botão "**Integrar**". O sistema exibirá uma tela de progresso da integração (em caso de mais de 3 registros marcados).
6. Ao final da integração, o sistema exibirá tela informando sobre o sucesso da integração. Clique no botão **Confirmar**.
7. Confirmar que apenas os registros não integrados é que constam ainda na tela.
8. Clicar no botão "**X**" no canto superior direito para encerrar a sub-rotina.
9. Clicar no botão "**X**" no canto superior direito para encerrar a rotina.
10. No módulo SIGAEIC, acessar o Menu **Atualizações\Portal Unico\Manutenção LPCO**.
11. Posicione sobre um processo de **LPCO** integrado no passo anterior e clique no botão "**Visualizar**".
12. Certifique-se de que os campos **Nro. LPCO**, Data e Hora da Integração e Chave de acesso foram preenchidos.
13. Clicar no botão Confirmar.
14. Clicar no botão "**X**" no canto superior direito para encerrar a rotina.

As informações devem ser ajustadas de acordo com as orientações descritas abaixo.  
  
**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |

| MV\_EIC0074 | Ambiente de Integração com o Portal Único 1=Produção, 2=Treinamento |
| MV\_EIC0073 | URL do Endpoint de Integração do Portal Único em Treinamento (URL principal das APIs de integração para treinamento.) |
| MV\_EIC0072 | URL do Endpoint de Integração do Portal Único em Produção (URL principal das APIs de integração para produção.) |
| EKO\_LPCO | Número do LPCO retornado pelo portal único Siscomex |
| EKO\_HORARG | Hora de registro da integração com o portal único Siscomex |
| EKO\_DATARG | Data de registro da integração com o portal único Siscomex |
| EKO\_CHVACE | Chave de acesso retornada pelo portal único Siscomex |

**Exemplo do procedimento**  
  
  
**Saiba mais**  
[Integração LPCO](https://tdn.totvs.com/pages/viewpage.action?pageId=578045218)   
[Procedimento para Implantação DUIMP](https://tdn.totvs.com/pages/viewpage.action?pageId=657762135)
