---
content_hash: 73baf884ce0c272f17d1cb0887447724a5052c71c44368f3c6af04d13eadf335
fetched_at: '2026-06-29T00:10:22.013135+00:00'
page_id: '496026630'
product: rm
source: tdn-rm
title: Meu Imóvel - Parâmetros do Aplicativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496026630
version: 31
---

Nesta tela, é possível configurar parâmetros que serão refletidos no aplicativo.

# **1) Procedimentos para configuração**

---

Os parâmetros do aplicativo podem ser acessados consultando os seguintes menus em **Ambiente / Parâmetros / Gestão de Imóveis:**

Parâmetros - Portal do ClienteParâmetros do Aplicativo

Os parâmetros do aplicativo são os seguintes:

* **URL de acesso externo ao Host:** Neste campo, deverá ser informada a URL externa do Host, que será enviada quando este capturar as parametrizações de primeiro acesso ao app, dentro do QRCode gerado.
* **Título do texto que será exibido na tela de Informações do Aplicativo:**O texto informado neste campo será exibido na tela de informações do Aplicativo. Ele tem um limite de **35 caracteres.**
* **Texto que será exibido na tela de Informações do Aplicativo:**O texto informado neste campo será exibido na tela de informações do Aplicativo. Ele tem um limite de **255 caracteres**, com no máximo de **20 quebras** de linhas,

Exemplo da tela de informações do Meu Imóvel com os parâmetros definidos.Na tela de informações também é exibida a versão do Aplicativo. Esta é uma informação muito útil para se detectar se o usuário está com o Aplicativo atualizado.

* **Fórmula do cálculo do Código de Barras (Protheus):** Este parâmetro possibilitará definir uma fórmula, que será utilizada para calcular o código de barras dos títulos disponiveis para pagamento no Protheus. Seguem algumas considerações sobre este parâmetro.
  + Esta opção somente estará disponível em ambientes cuja integração com o EAI1 esteja ativa e configurada;
  + Caso exista configuração ativa porém ainda sem uma fórmula definida nestes parâmetros, o Meu Imóvel não permitirá a cópia do código de barras;
  + Somente lançamentos cujo status da remessa seja igual a registrado ou remetido serão exibidos na visão de boletos do Meu imóvel;
  + Da mesma forma, somente lançamentos em aberto ou baixados parcialmente poderão ter seu código de barras copiado;

# **2) Exemplo de fórmula que calculará o código de barras / IPTE num ambiente integrado com o Protheus:**

---

c#

# **3) Consulta SQL (FÓRMULA\_PROTHEUS do exemplo acima)**

---

c#

Esta fórmula deverá ser sempre criada dentro do contexto do TOTVS Gestão Financeira, visto que as informações bancárias estão presentes na tabela FLAN

A sentença que compõe a fórmula poderá ser baseada na mesma sentença que é utilizada no relatório de boleto do Protheus
