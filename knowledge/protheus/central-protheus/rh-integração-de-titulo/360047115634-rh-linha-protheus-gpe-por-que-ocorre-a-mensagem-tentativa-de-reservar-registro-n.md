---
article_id: 360047115634
category: RH - Integração de Titulo
content_hash: 0dfd326e16dd6468342517f05d636b5e7b19f6c237dc29506967f69e26cb26d7
fetched_at: '2026-06-28T22:43:36.414661+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Por que ocorre a mensagem Tentativa de reservar
  registro no Alias em EOF Stack de chamadas em MSRLOCK.eof Controle de transações
  Habilitado
type: support-article
updated_at: '2025-07-21T20:21:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047115634-RH-Linha-Protheus-GPE-Por-que-ocorre-a-mensagem-Tentativa-de-reservar-registro-no-Alias-em-EOF-Stack-de-chamadas-em-MSRLOCK-eof-Controle-de-transa%C3%A7%C3%B5es-Habilitado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33616797164311)**Tempo aproximado para leitura: **00:02:00 min****Dúvida**Por que ocorre a mensagem: Tentativa de reservar registro no Alias em EOF Stack de chamadas em MSRLOCK.eof Controle de transações Habilitado?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Solução****Mensagem:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069576253)

**Conceito:**   
O controle de transação é uma ferramenta importante que garante a integridade de dados quando uma determinada operação é realizada no Banco de Dados.

O Protheus possuí o parâmetro **MV\_TTS** que quando ativado garante que este processo exista nos processos críticos de transação de arquivos. Detalhes: **[Controle de Transação - MV\_TTS](https://tdn.totvs.com/pages/viewpage.action?pageId=6814812)**

As alternativas existentes quando da atualização de tabelas são :

* Efetivar a transação - quando realizada com sucesso
* Voltar a status anterior (rollback) - desfaz toda a transação iniciada quando o final da transação não foi concluído com sucesso. Isto garante a total integridade dos dados.

**A mensagem "EOF Stack em MSRLOCK" indica que a rotina tentou reservar um registro para ser manipulado no processamento; mas o ponteiro da tabela estava em FIM DE ARQUIVO (MODO EOF) pois não localizou o dado procurado na Tabela.**  
Ou seja, algum dado (relacionado a este registro que está sendo processado) está inválido / não foi localizado, apresentando quebra de integridade.

É gravado um arquivo de log denominado msrlock.eof na pasta system. Para uma correta conferência, deve-se realizar o processo com a ocorrência em ambiente de homologação onde ocorra o problema, após apagar este registro (para eliminar dados gravados anteriormente).

**Exemplo:** Suponhamos que a mensagem ocorre ao tentar gerar / excluir um Doc. de Saída.  
Então algum dado relacionado com esse Doc de Saída está inválido / não foi localizado, apresentando quebra de integridade.  
Pode por exemplo ser algo inválido no cadastro do TES utilizado no Pedido de Vendas; pode ser o código do Cliente / Fornecedor / Loja estar registrado um código inválido, que não existe; pode conter um código de Produto no grid, ou um código de condição de Pgto, ou o código do Item, ou outro dado qualquer o qual não existe/ não é válido, etc....  
  
**Procedimento:**

**1º) Rastreamento do dado incorreto relacionado ao registro**

É necessário rastrear especificamente no ambiente para identificar qual registro da base está com o problema.  
Deste modo, a primeira análise é avaliar se os registros que está tentando processar possuem dados válidos no Banco, principalmente para a Tabela apontada no alerta e as relacionadas ao processo executado.

Recomenda-se realizar simulações para isolar o problema / o registro.  
Exemplo, inserir um registro idêntico na base de dados e verificar se o registro é gravado nas tabelas com os mesmos dados e se o problema também ocorre.

Este tipo de informação incorreta pode ter sido incluído ou por manipulação de dados no Banco (procedimento este não indicado) ou pela própria rotina sem ter ocorrido a validação adequada (possivelmente devido à uma das causas mencionadas abaixo).

**2º) Customizações / Personalizações em seu ambiente.**

* Personalização por Ponto de Entrada:  
  Algumas personalizações utilizam os comandos dbSeek, MsSeek, dbGoTo e etc. que desposicionam os registros de tabelas utilizadas nas rotina do produto padrão causando o problema de "EOF Stack em MSRLock". Para este caso recomendamos que utilize um RPO limpo sem customizações para verificar se o problema esta sendo causado por alguma personalização.  
    
  ![(ideia)](https://tdn.totvs.com/s/pt_BR/8100/4410012ac87e845516b70bc69b6f7a893eabaa5a/_/images/icons/emoticons/lightbulb_on.svg) Caso não seja possível utilizar um repositório limpo para o teste, é necessário habilitar em seu ambiente a chave IXBLOG=NORUN (Para informações acesse: <http://www.tdn.totvs.com.br/display/public/mp/Chave+IXBLOG>)  
  Registrar a linha de comando IXBLOG=NORUN no ini do server dentro da sessão do ambiente  
  Simular o processo e verificar se a inconsistência permanece!  
  Após a execução do procedimento a linha criada no \*.INI do server deve ser removida, pois pode causar baixa performance no sistema se mantida.  
    
  OBS: Caso ainda assim permaneça, é gravado um arquivo de log denominado msrlock.eof na pasta system.  
  Para a correta conferência, deve-se realizar o processo com a ocorrência em ambiente de homologação onde ocorra o problema, após apagar o arquivo já gravado no diretório (para eliminar dados gravados anteriormente).
* Personalização por Dicionário de Dados:  
  ![(ideia)](https://tdn.totvs.com/s/pt_BR/8100/4410012ac87e845516b70bc69b6f7a893eabaa5a/_/images/icons/emoticons/lightbulb_on.svg) Verificar se há customizações na Estrutura do Protheus, como por exemplo, Índices (SIX) ou gatilhos (SX7).  
  Realizar backup dos arquivos na Pasta System e recriar com um dicionário de dados padrão a atualizado. Refazer o processo.

**3) Inconsistência na rotina possivelmente causada por atualizações incompatíveis no ambiente**

Certificar-se de estar com últimas atualizações do Portal do Cliente. Em ambiente homologação testar com último RPO, Binários, DBACCESS, LIB e pacote quinzenal de atualizações. Verificar se neste cenário ocorre o problema.

**Observação:** Caso o ambiente esteja armazenado no Cloud Data Center da TOTVS, será necessário acionar pontualmente o Suporte Cloud mencionando os itens específicos que necessitam de intervenção do Cloud, para que forneçam os dados mencionados para análise.  
  
**Importante:**

Há procedimentos incisivos ao sistema em alguns dos processos mencionados, **que devem ser realizados por sua Equipe de TI** e, aconselhamos que caso tenha alguma dúvida no processo, solicite acompanhamento de um consultor Totvs!

**Os procedimentos indicados são utilizados para rastrear a possível causa da ocorrência**. Caso ainda ocorra apesar da devida realização dos procedimentos, **será necessário solicitar auxilio da equipe de Suporte Investigativo TOTVS** para que acesse remotamente a sua base, visando avaliação/ debug da rotina para investigá-la e identificar a origem do problema.

 

**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
