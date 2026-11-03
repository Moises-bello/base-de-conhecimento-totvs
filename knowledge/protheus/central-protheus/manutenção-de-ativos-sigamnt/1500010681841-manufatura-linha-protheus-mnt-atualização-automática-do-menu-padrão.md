---
article_id: 1500010681841
category: Manutenção de Ativos (SIGAMNT)
content_hash: d690c5e46abdc0e641efa03110038042c08acae221cd816a0e8bf545f779219a
fetched_at: '2026-06-28T22:42:32.781809+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Atualização automática do menu padrão
type: support-article
updated_at: '2021-06-02T12:59:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010681841-Manufatura-Linha-Protheus-MNT-Atualiza%C3%A7%C3%A3o-autom%C3%A1tica-do-menu-padr%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como ocorre a atualização automática do menu padrão?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - A partir da versão 12  
  
**Solução**Ao utilizar o padrão do módulo **Manutenção de Ativos - SIGAMNT**, as rotinas de alguns processos ficam indisponíveis para utilização. Para que estas fiquem disponíveis, deve-se ser habilitado os seguintes parâmetros:

* **MV\_NGMNTFR - Indica se a empresa irá utilizar o Gestão de Frota**
* **MV\_NGMNTCC - Indica se a empresa utiliza o Template de Construção Civil. Utilize S = Sim e N = Não.**
* **MV\_NG1FAC - Indica se utiliza Facilities ou Solicitação serviço. 1=Facilities;2=Solicitação**
* **MV\_NGINTER - Indica se esta integrado a outro ERP (L=Logix, R=RM, M=Mensagem Única, N=Não).**

O próprio Sistema pode identificar esta situação e atualizar o menu conforme os parâmetros citados sejam habilitados, entretanto para isso algumas premissas são necessárias.

1. **Menu padrão**: É necessário possuir o menu padrão, arquivo **SIGAMNT.xnu** armazenado em um diretório do Sistema.
2. **AppServer.ini**: Deve-se ser definido na seção **environment**utilizado, o diretório onde foi armazenado o menu padrão do módulo, este deve ser indicado na chave **StartPath**.
3. **Configurador**: Nos casos onde o ambiente não utiliza dicionário na base, é necessário que seja definido por usuário, que o caminho onde este obterá o menu será o mesmo definido na chave **StartPath**. Esta configuração já é a padrão do Sistema. Para ambientes com dicionário em base este item pode ser desconsiderado.

Com estes itens configurados, na primeira abertura do módulo será avaliado e recriado o menu seguindo as parametrizações definidas. Para os casos onde possa existir alguma customização própria nos arquivos de menu, está poderá ser aplicada após este processo de atualização automática.  
  
**Saiba mais**  
O menu padrão pode ser obtido por meio do *link:* [Menu Padrão](https://suporte.totvs.com/portal/p/10098/download?e=946739)
