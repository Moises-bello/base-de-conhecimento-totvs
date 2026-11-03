---
content_hash: dc59c2846bcd4db4bb29cb61faa053c229043abd2d58d3e27d4b67f1fdbb5867
fetched_at: '2026-06-29T00:05:59.447466+00:00'
page_id: '190518894'
product: rm
source: tdn-rm
title: RMFIS00005_Registro 0450 - Parametrização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=190518894
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** *11.82.3x* |
| **Processo** | **:** | SPED Fiscal - Registro 0450 |
| **Subprocesso** | **:** | Parametrização e Geração |
| **Data da publicação** | **:** | 25/06/2015 |

**Definição do Processo**

O objetivo deste documento é oferecer orientações sobre a parametrização e geração do Registro 0450, no arquivo texto do SPED Fiscal/EFD Contribuições.

**Parametrização Necessária**

É necessário criar um campo Complementar para o Lançamento Fiscal(Movimento) tanto no **TOTVS Gestão Fiscal**, como no **TOTVS Gestão de Estoque, Compras e Faturamento**(caso opere como RM Nucleus). Uma vez preenchido o campo no RM Nucleus e escriturado, o mesmo é integrado com o sistema fiscal automaticamente.

       Acesse: *Cadastros -> Campos Complementares -> Lançamentos Fiscais.* **Nome da Coluna**: INFCOMPLDOCFISCAL   **Tipo**: Texto

**LANÇAMENTO FISCAL**

No RM Liber, acesse o documento fiscal: Tributação -> Situações Tributárias -> Informações Adicionais - Campos Complementares.

No RM Nucleus, acesse: *Cadastros -> Campos Complementares -> Movimentos****:* Nome da Coluna**: INFCOMPLDOCFISCAL   **Tipo**: Texto(Exatamente, o mesmo campo do sistema fiscal).

**MOVIMENTO**

No Movimento, o campo deverá ser preenchido em Informações Adicionais -> Campos complementares.

**Importante**: Todos os campos alfanuméricos terão tamanho máximo de 255 caracteres, exceto se houver indicação distinta, onde, neste caso, este tamanho distinto prevalecerá.

Para mais informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](http://fluig.totvs.com/portal/p/10097/subject/rfiscal)****

**Canais de Atendimento:**

**Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
