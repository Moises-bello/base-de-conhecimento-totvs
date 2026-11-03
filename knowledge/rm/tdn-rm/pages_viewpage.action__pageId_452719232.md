---
content_hash: 161052f7fc204ed2e73741983f15dde82f0910e3302dade3172e8f508d841d99
fetched_at: '2026-06-29T00:10:04.681004+00:00'
page_id: '452719232'
product: rm
source: tdn-rm
title: Gerar XML Periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719232
version: 7
---

Neste módulo será gerada a estrutura de XML dos registros dos Eventos Periódicos para Integrar com TAF (Sistema da TOTVS responsável pela validação e transmissão dos dados para o governo).   
Além do que é dito acima, para os eventos que são relacionados aos funcionários, existirá a possibilidade de utilizar seleções de funcionários, onde poderá escolher os funcionários que desejar, ou apenas gerar os XML's já existentes na fila de eventos.  
   
Obs.: Os eventos serão considerados de acordo com a parametrização de execução do processo de Gerar XML.  
   
**Competência Atual -** Com este parâmetro será possível fazer com que a execução do processo considere a competência atual da folha para geração dos arquivos XML.  
**Atenção:** A existência de um período de apuração para a competência atual é obrigatório, caso contrário, o processo será finalizado com erro/aviso.

**Regerar XML -** Este parâmetro deve ser usado apenas quando for necessário regerar os XML's já existentes na fila de eventos periódicos para a correção de alguma inconsistência. Desta forma o processo é executado com melhor performance por não ser necessário a seleção de funcionário. O XML será regerado para todos os eventos existentes no período de apuração de acordo com a seleção de status e tipo de arquivo.

**Regerar eventos S-1298 e S-1299**: Este parâmetro deve ser utilizado para realizar a geração de um novo XML para os eventos S-1298 - Reabertura de Eventos Periódicos e S-1299 - Fechamento dos Eventos Periódicos existentes no período de apuração com status diferente de: 0 - Pendente, 1 - Gerado, 2 - Erro na Geração.

**Gerar novo XML para evento excluído através do S-3000** - Este parâmetro deve ser utilizado para realizar a geração de um novo XML para eventos que foram excluídos através do evento S-3000, existentes no período de apuração de acordo com a seleção de status e tipo de arquivo.  
   
**Atenção:**  
Para considerar os Autônomos do Fluxus, o usuário deverá parametrizar o sistema conforme passos a seguir:

* Informar os eventos do tipo Provento/Desconto em: "[Parametrizador](https://tdn.totvs.com.br/display/LRM/Gerar+XML) | [eSocial](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718787) | [Autônomos e Externos 1/2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719944)" e "[Parametrizador](https://tdn.totvs.com.br/display/LRM/Gerar+XML) | [eSocial](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718787) | [Autônomos e Externos 2/2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=463823367)".
* Quando for gerar o XML confirmar o parâmetro: "Gerar Autônomos Fluxus/Externos".
* Para auxiliar o usuário na geração dos arquivos , poderão ser gravados vários Perfis de Parâmetros.
* Os Perfis gravados poderão ser reutilizadas nas próximas gerações.

   
Considerações importantes na geração dos arquivos:  
   
Eventos Periódicos

|  |  |
| --- | --- |
|  | Como Fazer |

---

[Seleção de Coligadas -Parâmetro "Considerar Todas as Coligadas"](http://tdn.totvs.com/pages/viewpage.action?pageId=444607665)
