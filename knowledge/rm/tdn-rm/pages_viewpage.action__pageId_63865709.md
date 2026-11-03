---
content_hash: d00c8b6e0182422baaf1fb4dc7f5f4bd4e8cff8e196369095c499da9c38a6e85
fetched_at: '2026-06-29T00:11:06.986423+00:00'
page_id: '63865709'
product: rm
source: tdn-rm
title: Alterar Máscara do Número do Documento/Lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=63865709
version: 14
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS RM Liber                        **Versão:** 11.52 |
| **Processo** | **:** | Alteração da máscara do número do documento |
| **Subprocesso** | **:** | Alterando número do documento/lançamento fiscal |
| **Data da publicação** | **:** | 28/06/2013 |

Para realizar a alteração na máscara do documento, necessário acessar os parâmetros do sistema RM Liber e RM Nucleus, conforme passos a seguir:

Acesse o menu OPÇÕES – PARÂMETROS – GERAIS/TABELAS – IDENTIFICAÇÃO DE REGRAS DE APURAÇÃO – ICMS – AVANÇAR – ETAPA LANÇAMENTO FISCAL 1/7, campo "Máscara do número do documento".

* + Atenção aos caracteres válidos exibidos na imagem a seguir:

* + **Atenção:**O sistema emitirá uma mensagem de aviso ao processo:

**Após definir a máscara, e caso seja superior a seis (6) caracteres, o sistema exibirá uma mensagem de atenção, apenas orientando que em rotinas fiscais que consideram apenas seis caracteres (tamanho do nº documento), será consistido os números da direita para a esquerda.**

Alterando a máscara do número do documento  superior a 6 dígitos, o sistema irá truncar as seis últimas posições a direita.

Exemplo: 123456789 - será considerado "456789".

Obs.: Se a empresa trabalha com o RM Nucleus, orienta-se a manter a máscara do número documento igual a definida nos parâmetros do RM Liber e vice versa.   
 Para que o sistema grave a alteração realizada, necessário avançar etapa por etapa dos parâmetros até conclusão do processo e realizar logout/login no sistema.

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal);
