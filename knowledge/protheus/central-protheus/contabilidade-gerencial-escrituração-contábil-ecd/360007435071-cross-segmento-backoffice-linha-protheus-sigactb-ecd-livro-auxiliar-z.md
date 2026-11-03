---
article_id: 360007435071
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: d0d005c4cedcd32dc0b19ce77026f23830bbef6726d3e15da9a644a382939778
fetched_at: '2026-06-28T22:40:44.286633+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD  LIVRO AUXILIAR
  Z '
type: support-article
updated_at: '2022-04-01T16:26:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007435071-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-LIVRO-AUXILIAR-Z
---

**Dúvida**Montagem do livro auxiliar Z Razão auxiliar da subconta ECD

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**

Z – Razão Auxiliar (Livro Contábil Auxiliar conforme leiaute definido nos registros I500 a I555).  
  
**1º**Verifique o cadastro das contas correlatas  
**[http://www.tdn.totvs.com/display/public/PROT/ECD0029\_SUBCONTAS\_CORRELATAS](http://tdn.totvs.com/display/public/PROT/ECD0029_SUBCONTAS_CORRELATAS)**  
**2º**  
<http://tdn.totvs.com/pages/releaseview.action?pageId=187531745>  
<http://tdn.totvs.com/display/public/PROT/ECD_SPED_CONTABIL_Alteracoes_para_Leiaute_4_00>  
Razão de sub contas auxiliar (**raz\_aux\_subcta\_ctb.txt**). é um modelo disponibilizado pela TOTVS, podendo ser personalizado conforme necessidade do contribuinte.   
**Obs : a configuração do arquivo deve ser feita de acordo as informações que serão entregues (preenchidas manualmente)**  
  
Modelo Razão Auxiliar das SubContas:  
**<http://tdn.totvs.com/pages/releaseview.action?pageId=235331339>**  
  
<http://tdn.totvs.com/display/public/PROT/ECD0025_EXEMPLO_PREENCHIMENTO_DO_RAS_PARA_AVP>  
  
Para utilização dos arquivos deve-se acessar o modulo SIGACFG (Modulo Configurador) seguindo os passos abaixo:  
-gravar o arquivo MOED\_FUNC\_E\_RAZ\_AUX\_SUBCTA\_CFG\_MILE.XML do pacote da ECD no diretório /System  
Ambiente-> Aceleradores-> Mile->Layouts(CFGA600).   
Dentro da rotina deve seguir as opções:  
Ações Relacionadas-> Layouts-> Importar à Procurar pelo arquivo “moed\_func\_e\_raz\_aux\_subcta\_cfg\_mile.xml” à Selecionar o mesmo e confirmar sua importação.   
  
<http://tdn.totvs.com.br/display/framework/MILE+-+Model+Integrator+Layout+Engine>  
**3º**  
  
Após isso, acessar o módulo SIGACTB (Contabilidade Gerencial), via opção de menu:  
  
Atualizações-> Escrituração Cont.-> Cadastros-> Layout Auxiliar(CTBS100).  
  
Dentro desta rotina, deve ser seguir as opções: Ações Relacionadas-> Outros-> Importar.  
  
Na tela que será apresentada, deve-se utilizar o campo “Arquivo” para selecionar o arquivo TXT “**raz\_aux\_subcta\_ctb.txt**” e, após a escolha, clicar no botão “Importar”. Com isso, tem-se a estrutura do leiaute auxiliar cadastrado.   
  
<http://tdn.totvs.com.br/display/public/PROT/ECD_SPED_CONTABIL_Alteracoes_para_Leiaute_4_00>  
<http://tdn.totvs.com.br/pages/releaseview.action?pageId=187531745>  
  
**4 º**Após gerar o arquivo – selecione as contas  
  
![](https://totvssuporte.zendesk.com/attachments/token/QMBNGJqZJjHkZCGqpArFHOwa0/?name=inline-507911471.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/QoNH0VcO1JB8Xen6pHKzjJlqn/?name=inline-1043532472.png)​
