---
article_id: 360022157031
category: TAF - eSocial -TSS
content_hash: 8bfa321e1b6171f8e6d05171529e33d08420e4d06096ce51795193189e35c5b6
fetched_at: '2026-06-28T22:45:21.912669+00:00'
product: protheus
section_id: 1500001536761
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Banco de dados do TSS crescendo demasiadamente
  impactando a transmissão dos eventos
type: support-article
updated_at: '2026-06-26T12:12:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022157031-RH-Linha-Protheus-TAF-eSocial-Banco-de-dados-do-TSS-crescendo-demasiadamente-impactando-a-transmiss%C3%A3o-dos-eventos
---

**Dúvida**Banco de dados do **TSS** crescendo demasiadamente, impactando a transmissão dos eventos ao **eSocial**, ficando com o status "Aguardando retorno do governo".  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - TSS - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse a tabela **TSS0004** do **TSS**, nesta tabela é gravado os logs (rastros) de transmissão do **TSS**, verifique se existe grande quantidade de registros gravados nesta tabela;   
  
2. Foi realizada uma melhoria pelo desenvolvimento do **TSS**, para habilitar o **parâmetro MV\_PROCLOG** na **tabela SPED000** do **TSS**;

SELECT \* FROM SPED000 WHERE PARAMETRO = 'MV\_PROCLOG'

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071260674)

Obs: caso o **parâmetro MV\_PROCLOG** não exista, o mesmo pode ser inserido/criado sem problemas via APSDU, basta ir ate a ultima linha da tabela **SPED000** e clicar com a seta do teclado para baixo, nesse momento será apresentada uma tela com a mensagem "Incluir registro?", clique em "Sim" e inclua-o.

Importante:

Com o parâmetro **MV\_PROCLOG=2** na tabela **SPED000** do **TSS,** não será gravado nenhum log na tabela **TSS0004,** porém se for apresentado algum erro pelo **eSocial** na qual teve retorno como inconsistente, não será possível identifica-lo na tabela, mas é possível visualizar a inconsistência no Painel Esocial de transmissão de eventos do **TAF**;

**Obs.:   
MV\_PROCLOG=1 - HABILITADO  
MV\_PROCLOG=2 - DESABILITADO**

3. Caso habilite no arquivo **appserver.ini** do **TSS**, a chave **LOG\_PERIOD** na seção [**SPED**], os logs gravados na tabela **TSS0004** serão deletados da tabela no prazo determinado;

**Exemplo**: Se a chave **LOG\_PERIOD** estiver com o valor igual a 3, (**LOG\_PERIOD**=3), isso significa que a cada 3 dias na tabela **TSS0004**será removido os logs nela contidos.

Se tiver muitos registros na tabela e com o parâmetro habilitado não deletar, pode limpar os registros e fazer o acompanhamento.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360019127232)

4. Temos a documentação a seguir relacionada à tabela **TSS0004**, que representa a tabela de rastreamento do **TSS**.

<http://tdn.totvs.com.br/pages/releaseview.action?pageId=417698432>
