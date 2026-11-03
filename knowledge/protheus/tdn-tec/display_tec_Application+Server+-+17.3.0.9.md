---
content_hash: 59e293209d273465f7ffea6993f7e8e19a725f23d1e9c2814e7d3be3b2009d55
fetched_at: '2026-07-02T19:24:24.240856+00:00'
page_id: '469458093'
product: protheus
source: tdn-tec
title: Application Server - 17.3.0.9
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.9
version: 8
---

GreenEXPEDIDO

# Correção

 Segunda chamada ao BasicPublish trava aplicação

Problema: declarar a queue sem o nome ele estava duplicando o nome, como era fila exclusive, e estava usando outro correlation, ele travava.   
  
Solução: Foi corrigido o gerador randomico de nomes, não gerando mais nome duplicados.

Referente ao chamado: TTEC-2640

 Variáveis modulares 4GL apresentam erro quando chamadas fora de escopo principal

Incidente:  
Variaveis modulares, quando declaradas em um fonte, que é acessado por uma function, ficam fora de escopo, apresentando como "não definidas"; sendo chamadas pelo escopo principal, funcionam normalmente.  
  
Solução:  
Existia um conflito de comportamento entre as variaveis do mesmo tipo no ADVPL, que causou um efeito colateral. Para contornar o problema, foi alterado para que este se comporte apenas no 4GL.

Referente ao chamado: TTEC-2809

 Não exibe erro de compilação em função com ausência de RETURN

Incidente:  
Uma função sem 'return' não apresenta erro de compilação.  
  
Solução:  
Criado controle para apresentar o erro " Statement unbalanced brackets in <<FUNÇÃO>>"

Referente ao chamado: TTEC-2812

 WritePProString parametrização indevida

Incidente: Quando o valor do segundo parâmetro é vazio ("") a gravação da chave no INI ficava incorreta  
  
Solução: Correção da função para tratamento do valor vazio no segundo parâmetro.

Referente ao chamado: TTEC-2990

 HTTP Server não respeita o DefaultPage para caminhos diferentes do raiz

Incidente: Busca de Páginas default não é respeitado quando é informado path na URL.  
  
Solução: Inserido tratamento para que se página não for informada a página default será procurada no path informado.

Referente ao chamado: TTEC-3028

 Compilação - Mensagens de warning não são exibidas corretamente

Incidente: Mensagens de warning não eram exibidas quando um codeblock era declarado.  
  
Solução: Exibição das mensagens de warning independente do uso de codeblock.

Referente ao chamado: TTEC-3036

 Memória do Appserver cresce exponencialmente ao aplicar patch

Incidente:  
Ao utilizar a opção "Aceito somente os fontes atualizados", a memoria do server cresce exponencialmente ao aplicar patch.  
  
Solução:  
Limpado lista e release de cada programa ao termino de cada arquivo do patch aplicado.

Referente ao chamado: TTEC-3039

 Erro ao trocar de empresa/filial por dentro do sistema

Incidente:  
Ao utilizar a função interna do ERP Protheus, é apresentado o erro "Invalid mask value(s)" mas a mascara passada é valida  
  
Solução:  
  
Corrigido para checar apenas o que é necessário: somente conter entre os caracteres EFU, e ter pelo menos um F

Referente ao chamado: MTEC-2235

 Problema Na Função SPF\_CopyTo no Linux

Incidente: Função Ctree SPF\_CopyTo apresentando erro para cópia de arquivos.  
  
Solução: Corrigido alterando variável tipo LONG para 4 bytes (requisito da FairCom).

Referente ao chamado: MTEC-2388

 TCheckBox executa bChange sem necessidade em algumas situações

Incidente: Em algumas situações o bloco de código bChange do TCheckBox é executado sem que o estado desse componente tenha de fato sido alterado.  
  
Solução: Foi aplicada uma correção que consiste em avaliar o estado do componente TCheckBox durante a sincronia de valores entre o SmartClient e AppServer. Se o valor for o mesmo que o server já possui, o bloco de código bchange não é executado.

Referente ao chamado: MTEC-2431

 [ISSUE][P12][ A TELA DO &quot;NÃO SOU UM ROBÔ&quot; NÃO É FECHADA AUTOMATICAMENTE AO CONSULTAR O MASHUP DA RECEITA FEDERAL POR CNPJ ]

Incidente: Tela "Não sou um robô" não é fechada automaticamente

Solução: Correção na comunicação do componente tWebEngine.

Referente ao chamado: MTEC-2443

 Após executar um \_CopyFile de uma tabela CTREE a tabela continua lockada

Incidente: Falha de abertura de um arquivo ctree caso o mesmo tenha sido copiado.  
  
Solução: Inserido chamada de rotina de Rebuild de Index nessa situação para que os indices tenham seus nomes acertados após a cópia.

Referente ao chamado: MTEC-2447

 Erro no inicio de validação da conexão - BROKER

Incidente: Geração de core na inicialização de dois brokers com o mesmo nome de serviço  
  
  
Solução: Remoção da geração de exceção na inicialização do serviço

Referente ao chamado: MTEC-2454

 [] - Erro CtreeServer no Primeiro acesso (Lobo Guara) no LINUX RED HAT

Incidente:  
  
Falha na execução da rotina de limpeza de arquivos temporarios c-Tree, disparada no primeiro login do primeiro usuario em ambiente usando c-Tree Server Linux 64 bits com APPServer Lobo Guará em Linux.   
  
Solução:  
  
Copiar o arquivo [libctreecb.so](http://libctreecb.so) (64 bits ) distrobuído originalmente com o Protheus 11 para a pasta do c-tree Server no Linux. A falta deste arquivo é responsável diretamente pela ocorrência. De qualquer modo, como o Application Server foi projetado para conseguir funcionar e identificar corretamente a presença da [libctreecb.so](http://libctreecb.so) no c-Treee Server Linux 64 bits, e conseguir trabalhar sem erro mesmo que este arquivo não esteja presente, foi alterada a forma de validação da versão do c-Tree Server para O Application Server Lobu Guará, disponível a partir da próxima build oficial.

Referente ao ticket Zendesk:   
Interno: MTEC-2490
