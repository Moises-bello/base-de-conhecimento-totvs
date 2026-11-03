---
content_hash: e72c8122f13d5eac3986445315e1008a2065c4985876e2942bf0ae488b5eec0d
fetched_at: '2026-06-29T00:11:37.933726+00:00'
page_id: '780780832'
product: rm
source: tdn-rm
title: TCGI - Ações de Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=780780832
version: 11
---

**Ações de Cobrança**

As ações serão utilizadas para realizar a comunicação com o Cliente/Fornecedor, será possível  cadastrar vários tipos de ações de cobrança. 

Dicas Importantes.

* As ações de cobrança podem ser utilizadas avulsas, isso traz uma maior flexibilidade para criar ações que possibilitem cobranças ativas (antes que a parcela vença por exemplo).
* Para isso a ação deve ter o seu filtro criado, obedecendo a regra desejada e deverá ser agendado a execução do processo através do controle de jobs do RM, utilizando a execução do processo (Gerar Ação Manual de Cobrança).   
  **Exemplo:** No filtro da tela "Gerar Ação Manual de Cobrança", deverá ser criado um filtro com as regras "Data Vencimento = $Hoje + 5" e "**Status** Financeiro diferente de **quitado**", assim, sempre que a ação agendada for executada o filtro trará as parcelas que irá vencer dentro dos próximos 5 dias e então será disparado o "Tipo Ação Cobrança" definida para os títulos do filtro. O sistema não realiza nenhum filtro interno, portando, toda condição deverá ser feita via filtro da visão do financeiro
Novidade!

* A partir do Release 12.1.2310, é possível de se executar as ações de cobrança para apenas um ou para todos os lançamentos em atraso, habilitando este comportamento diretamente no parâmetro de Cobrança ***[Definir Valor Default Para Cadastro Da Ação](https://tdn.totvs.com/pages/viewpage.action?pageId=781851010)***, ou também em cada uma das ações de cobrança descritas abaixo, através da opção ***Executar a ação de cobrança apenas para o lançamento mais antigo***:

* **[Envio de E-mail](https://tdn.totvs.com/display/LRM/TCGI+-+Envio+de+E-mail)**
* **[WhatsApp](https://tdn.totvs.com/display/LRM/TCGI+-+WhatsApp)**
* **[Envio de SMS](https://tdn.totvs.com/display/LRM/TCGI+-+Envio+de+SMS)**
* **[Abertura de Atendimento de Cobrança para contato com Cliente](https://tdn.totvs.com/pages/viewpage.action?pageId=780781177)**
