---
article_id: 31688498403735
category: Financeiro - Conciliação de Vendas
content_hash: 21a1caa8abecb8884d915ae104aaeededd30625730b5724a16a95a4b59a0cb08
fetched_at: '2026-06-28T22:37:26.293688+00:00'
product: protheus
section_id: 35058743504791
source: central-protheus
title: Cross Segmentos - Linha Backoffice Protheus - FINA918 - Não existe o parâmetro
  para a Empresa/Filial, o movimentação será conciliado
type: support-article
updated_at: '2026-02-04T13:27:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31688498403735-Cross-Segmentos-Linha-Backoffice-Protheus-FINA918-N%C3%A3o-existe-o-par%C3%A2metro-para-a-Empresa-Filial-o-movimenta%C3%A7%C3%A3o-ser%C3%A1-conciliado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31688498401431) Tempo aproximado para leitura: **00:10 min**  
  
**Ocorrência**  
No módulo Financeiro, ao tentar realizar a conciliação **(FINA916/FINA918)** e marcar os registros, apresenta a mensagem **"Não existe o parâmetro para a Empresa/Filial, o movimento não será conciliado, continua exibindo o alerta?"**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31688640070679)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois o campo de **Código da Administradora** nos registros de conciliação está diferente do código informado na rotina **LOJA075 - Administradoras Financeiras.**  
  
**Solução**

**1.** Avaliar qual é o código de **Administradora Financeira** que está sendo apresentado na tela de conciliação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31688624427543)

**2.** Acessar a rotina **LOJA075** e verificar se o mesmo código de administradora está sendo informado.   
  
**3.** Cadastrar o código igual à rotina **FINA918** e marcar posteriormente os registros, não será mais exibida a mensagem.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31688640072087)  
  
**Saiba mais**  
[Conciliador Pagamentos e Vendas - Financeiro (Contas a Receber) - P12](https://tdn.totvs.com/display/PROT/Conciliador+Pagamentos+e+Vendas+-+Financeiro+%28Contas+a+Receber%29+-+P12)
