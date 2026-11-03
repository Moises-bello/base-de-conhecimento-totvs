---
content_hash: 4386c23dd961e5b7068ac0030fc87405f9b9d39f976f7e18bd30a24004031974
fetched_at: '2026-06-29T00:09:36.789402+00:00'
page_id: '425459521'
product: rm
source: tdn-rm
title: Monitor da Fila de Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459521
version: 3
---

**Monitor da Fila de Integração**   
 Os sistemas integrados trocam mensagens ente si para sincronizar seus dados.   
    
   
    
 As mensagens trocadas são gerenciadas pelo Monitor da Fila de Integração do TOTVS Business Conector.  
    
 É necessário que elas tenham seu envio ou recebimento processados através dos respectivos Serviços. Também é fundamental que a troca de mensagens seja gerenciada através do Monitor da Fila de Integração, para que mensagens que tenham sido trafegadas ou processadas com erro tenham o devido acompanhamento.  
    
 No Monitor da Fila de Integração ficam listadas todas as mensagens trocadas durante a integração dos aplicativos, permitindo ao administrador do sistema acompanhar em detalhe a troca de mensagens e realizar o gerenciamento das mesmas. É através do Monitor que é possível gerenciar o que foi executado pelos Serviços.  
    
 Para cada mensagem é possível ver diversas informações, como por exemplo Produto, Cód. Entidade, Entidade, Status, Versão, Data, Identificador, Coligada, Filial, entre outros.  
    
 É possível escolher as colunas que se deseja visualizar, bem como a disposição das mesmas na visão e realizar agrupamentos. Ao dar duplo clique em uma mensagem, é aberta uma visão contendo:

* **Mensagem:** A mensagem XML que foi enviada ou recebida. No quadro inferior, será exibida a mensagem de erro, caso o mesmo ocorra.
* **TOTVS Message:** A mensagem já no formato de mensageria padrão.
* **Retorno:** O retorno das mensagens enviadas

***Nota:*** *As abas TOTVS Message e Retorno só estarão preenchidas caso a integração utilize o novo padrão de mensagens TOTVS.*

No Monitor é possível executar os processos:

* **Reprocessar Fila Integração:** O processo prepara os registros selecionados com status "Erro", para que sejam enviados ou recebidos novamente. Dessa forma as mensagens que não foram enviadas ou recebidas devido a algum problema podem ter seu envio/recebimento reprocessados.

***Nota:*** *Caso o parâmetro "Ativar Log Debug" esteja ativo, o processo irá reprocessar qualquer mensagem selecionada, independente de seu status. Este recurso deve ser habilitado pelo supervisor do sistema apenas em casos específicos ou por solicitação do suporte RM.*

* **Exportar XML (Integração):** O processo permite gerar uma mensagem no formato XML. Ao executá-lo, é aberta uma visão solicitando para definir a pasta onde deseja salvar o arquivo XML. Após concluído o processo, basta ir no local indicado e abrir o arquivo.
