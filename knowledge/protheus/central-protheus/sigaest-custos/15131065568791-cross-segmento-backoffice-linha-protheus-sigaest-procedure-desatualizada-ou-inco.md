---
article_id: 15131065568791
category: SIGAEST - CUSTOS
content_hash: c475a1625384432f1e0bb7ed252223f79417967f95ad55b7269758a42ae98189
fetched_at: '2026-06-28T22:39:02.325169+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada
  ou Incompatível
type: support-article
updated_at: '2026-06-17T21:21:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel
---

O artigo explica as diferenças entre Procedures Desatualizadas e Incompatíveis no Protheus SIGAEST. Procedures desatualizadas não impedem o uso, mas podem ser atualizadas para a versão mais recente. Procedures incompatíveis têm assinaturas divergentes da rotina AdvPL, impossibilitando seu uso até que sejam compatibilizadas. Recomenda-se reinstalar procedures após alterações em campos de tabelas relacionadas a saldos e movimentos. Links para atualização e solução de problemas são fornecidos.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17519211310487) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Quais as diferenças entre Procedures Desatualizadas e Incompatíveis? É possível utilizar as rotinas?

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38946719309463)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões

**Solução**

Primeiro ponto importante, é validar se a sua Central de Atualização contempla da ultima versão disponivel: [Central de Atualizações Protheus](https://suporte.totvs.com/portal/p/10098/download?e=946864)

Além disso, caso tenha recentemente ajustado o tamanho ou grupo de campos relacionados às seguintes tabelas ***SB1, SB2, SB8, SD1, SD2, SD3, SD4, SD5, SDB, SBJ, SBK, SB9, SDD, SDC, SDA, SBF***, além das demais que envolvam saldos ou movimentos de Estoque, **é** ***imprescindível realizar a** **reinstalação das procedures de forma geral**.*

Essa ação é necessária para adequar os tamanhos dos campos do seu dicionário de dados no Procedure, pois a ausência dessa atualização pode gerar problemas em consultas, relatórios, saldos iniciais, entre outros.

**Certifique, que as 3 opções da engrenagem estejam Desmarcadas! caso não, desmarque, e então clique em confirmar.**

![procedengrena.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41084108663831)

Feito isso, basta selecionar o Grupo de empresa, e marcar os processos desejados, após clicar no menu de instalação e aguardar o processo, Caso gerado algum erro, abra o campo MEMO no final da instalação do processo e envie ao Suporte.

**Realizou o processo, mas as procedures não foram instaladas?** Solicite ao seu analista DBA que valide se existem os processos instalados na base de dados, pode haver resquiços de instalações anteriores, que precisam ser removidos para uma nova instalação.

[PEST06018 - Stored Procedures utilizadas no produto Estoque e Custos](https://tdn.totvs.com/x/wi3AFQ)

Aqui no Estoque Custos, validamos os processos de **14 a 22**, cada area cuida das suas respectivas procedures.

**Status Desatualizado e Incompatível dos Procedures:**

![sps_outdated.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38940696209303) **DESATUALIZADO**: O processo instalado no ambiente não está na sua versão mais recente disponibilizada pela TOTVS. Isso significa apenas que o IDSPS do pacote instalado é inferior ao IDSPS do último pacote homologado. Um pacote que está desatualizado não representa um erro e sua atualização não é obrigatória ou urgente. Um pacote de procedures com este status pode perfeitamente ser executado por sua rotina AdvPL.

**Solução:**

Para realizar a atualização das Procedures basta seguir as orientações descritas no link: [**ATUALIZAR O PROCESSO**](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes#StoredProceduresNovogerenciadordepacotes-instalando_pacotes), basicamente voce pode dar um duplo clique na procedure, e validar se existe a opção "Buscar Atualizações", que vai lhe direcionar para o pacote pontual para atualização do processo.

**![sps_not_compatible.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38940669209367) INCOMPATÍVEL:** Nesta situação as assinaturas do processo e da rotina AdvPL (consulte tópico [Visualizando detalhes](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes#StoredProceduresNovogerenciadordepacotes-visualizando_detalhes)) são incompatíveis. Isso significa que a rotina AdvPL que faz a chamada para as procedures não poderá utilizá-las. Ao tentar executar uma rotina que esteja incompatível com seu processo de stored procedures, o usuário receberá uma mensagem de Incompatibilidade.

**Solução:**

A solução nestes casos envolve as ações descritas no link: [**COMPATIBILIZAR AS ASSINATURAS**](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes#:~:text=Solu%C3%A7%C3%A3o%3A%20COMPATIBILIZAR%20AS%20ASSINATURAS)

![](https://tdn.totvs.com/download/thumbnails/651665430/sps_updated.png?version=1&modificationDate=1657717600227&api=v2) **ATUALIZADO:** O processo instalado no ambiente está atualizado com a última versão disponível em comparação ao pacote que está no **RPO** (**modo offline**) ou em relação ao pacote disponível na **Central de Atualizações** (**modo online**).

**Solução:**

Nenhuma ação é necessária neste caso.

![](https://tdn.totvs.com/download/thumbnails/651665430/sps_not_rated.png?version=1&modificationDate=1657717566273&api=v2) **NÃO AVALIADO:** Neste caso o processo instalado no ambiente não pôde ser comparado com o que está embarcado no RPO (modo offline) nem com o que está disponível na Central de Atualizações (modo online). Este status é muito peculiar e não ocorrerá com frequência, exceto nas seguintes situações: [**NÃO AVALIADO**](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes#:~:text=N%C3%83O%20AVALIADO%3A%20Neste%20caso%20o%20processo%20instalado%20no%20ambiente%20n%C3%A3o%20p%C3%B4de%20ser%20comparado%20com%20o%20que%20est%C3%A1%20embarcado%20no%20RPO%20(modo%20offline)%20nem%20com%20o%20que%20est%C3%A1%20dispon%C3%ADvel%20na%20Central%20de%20Atualiza%C3%A7%C3%B5es%20(modo%20online).%20Este%20status%20%C3%A9%20muito%20peculiar%20e%20n%C3%A3o%20ocorrer%C3%A1%20com%20frequ%C3%AAncia%2C%20exceto%20nas%20seguintes%20situa%C3%A7%C3%B5es%3A)

![](https://tdn.totvs.com/download/thumbnails/651665430/sps_not_installed.png?version=1&modificationDate=1657717547047&api=v2) Indica que o processo não está instalado.

**RELATÓRIO DE LOG**  
Caso tenha realizado as ações descritas na documentação e o Procedure permaneça com o Status incorreto, é possível gerar um [**RELATÓRIO DE LOG**](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes#:~:text=coluna%20Detalhes%3A-,Relat%C3%B3rio%20de%20Log,-No%20bot%C3%A3o%20Outras). O Relatório de Log pode indicar o erro na atualização das Procedures.

Veja também alguns incidentes já mapeados: [**Resolução de problemas pontuais**](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes#:~:text=an%C3%A1lise%20de%20problemas.-,Resolu%C3%A7%C3%A3o%20de%20problemas%20pontuais%20sem%20necessidade%20de%20contato%20com%20suporte%20TOTVS,-Alguns%20problemas%20ocorridos).

Documentações técnicas de referência sobre a nova Gestão de Procedures:

* [Stored Procedures utilizadas no produto Estoque e Custos](https://tdn.totvs.com/x/wi3AFQ)
* [Stored Procedures - Novo gerenciador de pacotes](https://tdn.totvs.com/x/FqDXJg)
* [Central de Atualizações - Protheus](https://tdn.totvs.com/x/OpamHw)

**Saiba Mais:**

[*SIGAEST - Como instalar as Stored Procedures?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009382821-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-instalar-as-Stored-Procedures-)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
