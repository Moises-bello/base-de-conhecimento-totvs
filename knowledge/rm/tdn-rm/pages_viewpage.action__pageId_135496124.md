---
content_hash: 61e5ebab3d2aec3d6312a9e84d1bd356b78522d60df957f4408bf66a26f8b6fd
fetched_at: '2026-06-29T00:05:55.351189+00:00'
page_id: '135496124'
product: rm
source: tdn-rm
title: NFS-e - Município não homologado para esta operação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=135496124
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NFS-e                        **Versão:***todas* |
| **Processo** | **:** | Envio de NFS-e |
| **Subprocesso** | **:** | Município não homologado para esta operação |
| **Data da publicação** | **:** | 23/08/2014 |

**Introdução:**

**Ao tentar enviar uma NFS-e o sistema apresenta a seguinte mensagem de erro:** Não foi possível enviar a nota.

Nenhuma NFS-e foi enviada.

Município não homologado para esta operação. Para maiores esclarecimentos procure o suporte Totvs.

**Dicas:**

1 - Verifique através do link abaixo se o município está homologado:

<http://tdn.totvs.com/pages/releaseview.action?pageId=4814340>

**2 -** Acesse o RM Nucleos no seguinte menu: Opções | Parâmetros | RMNucleus | Integrações | Fiscal | Parâmetros por filial | Ambiente.

No campo “Classificação Município” deve ser selecionada a tabela de classificação de município, esta tabela varia de acordo com cada município que poderá ser IBGE (ABRASF) ou SIAFI (DSFNET).

**3 -** Verifique se o código IBGE possui 7 dígitos:

Cadastro | Tabelas auxiliares | Municípios – edite o cadastro do município

Anexos | codificação do Município

4 - Caso o município esteja homologado execute a configuração do servidor Murshup conforme link abaixo:

<http://tdn.totvs.com/pages/releaseview.action?pageId=64651845>

**5** -  Caso já tenha realizado o configuração do Murshup realize o seguinte processo:

Acesse o menu:  utilitários | SPED | NFSe (municipal) em seguida Processos | Atualização de Municípios Homologados

Nesta tela existem duas listagens: ao lado esquerdo corresponde aos municípios em que o sistema RMNucleus já considera como homologados e ao lado direito a listagem de todos os municípios que a TOTVS já disponibilizou utilização remotamente.

Obs: É necessário que o município que esteja parametrizando seja apresentado ao lado esquerdo da imagem, caso contrário a inconsistência continuará a ser apresentada.

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
