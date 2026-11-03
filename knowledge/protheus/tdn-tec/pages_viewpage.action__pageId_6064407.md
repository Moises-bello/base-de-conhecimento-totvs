---
content_hash: f009dbab5712428802946f978c1be49e6e630c2fa39f2d3818f8680385384256
fetched_at: '2026-07-02T19:24:26.694407+00:00'
page_id: '6064407'
product: protheus
source: tdn-tec
title: Instalação do TOTVS  Application Server com o servidor ADS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=6064407
version: 4
---

BLOCK

Instalação do TOTVS Application Server com o servidor ADS

## Instalação do TOTVS | Application Server com o servidor ADS

### Instalação do servidor ADS

1. Com o CD de instalação do ADS, inicie a instalação do TOTVS | Application Server no sistema operacional correspondente, escolhendo a opção ***All Others Countries***.
2. Quando solicitado, informe o ***Serial Number*** e ***Validation Code*** enviado pelo fornecedor.
3. A opção ***ANSI character***, normalmente, está como <Default on Machine>. Altere para **Engl(Amer)**.
4. Para ***OEM character set***, selecione **USA**.

### Configuração do servidor ADS

1. No *Advantage Configuration Utility*, verifique os parâmetros de limite (*Work Areas*, *Tables*, Índices e *Locks*).  
    A explicação destes parâmetros pode ser encontrada no *help* do produto ou no arquivo \bin\appserver\adslocal.cfg (resumo).
2. Configure o valor de***Worker Threads*** para 64.  
    Verifique estes valores, no início da utilização do sistema, para definir se é necessário aumentar ***–*** ***Max Used*** está próximo de ***Configured*** ou há requisições rejeitadas (*Reject*).

   | Cuidado |
   | --- |
   | Alguns destes parâmetros têm impacto na utilização de memória da máquina. |

### Veja também

---

[Versão ACE - Advantage Client Engine](http://tdn.totvs.com/pages/viewpage.action?pageId=6064406)
