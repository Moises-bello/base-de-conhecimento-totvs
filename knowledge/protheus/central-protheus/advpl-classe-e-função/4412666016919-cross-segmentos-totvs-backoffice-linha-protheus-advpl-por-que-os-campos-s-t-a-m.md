---
article_id: 4412666016919
category: ADVPL - Classe e Função
content_hash: c2ba20eabd99686967d353dd5564ace9dd9d702142e53af4e830704857d8d6ea
fetched_at: '2026-06-28T22:40:21.633359+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Por que os campos
  S_T_A_M_P e I_N_S_D_T não estão sendo criados no banco de dados
type: support-article
updated_at: '2023-11-10T15:10:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412666016919-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Por-que-os-campos-S-T-A-M-P-e-I-N-S-D-T-n%C3%A3o-est%C3%A3o-sendo-criados-no-banco-de-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18973591575319) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Por que os campos **S\_T\_A\_M\_P** e **I\_N\_S\_D\_T** não estão sendo criados no banco de dados?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões

**Solução**Para o correto funcionamento do comando **SETAUTOSTAMP**, é necessário que o comando **SETUSEROWSTAMP**esteja habilitado, senão o campo **S\_T\_A\_M\_P**não será criado. O mesmo processo ocorre para criação do campo **I\_N\_S\_D\_T**.

```
User Function Exemplo()  
  
Local nI, cConfig, aConfig   
  
//Cria uma nova conexão com um banco (SGBD) através do DBAccess  
TCLink()   
  
//Habilita o Dbaccess e acrescentar o campo STAMP nas novas tabelas  
TCConfig('SETUSEROWSTAMP=ON')   
  
// Habilita criar o campo para tabelas já existentes (Para usar esse segundo comando ( AUTOSTAMP ) , você deve primeiro habilitar o primeiro (USEROWSTAMP)  
TCCONfig("SETAUTOSTAMP=ON")   
  
// Faz o Dbaccess acrescentar a coluna sem precisar recriar a tabela  
TCRefresh("SRCT10")   
  
//Após execução desligar as chaves para não criar em outras tabelas do sistema desnecessárias   
 TCCONfig("SETUSEROWSTAMP=OFF")   
 TCCONfig("SETAUTOSTAMP=OFF")   
  
//Encerra a conexão especificada com o DBAccess  
TCUnlink()   
  
Return
```

**Saiba Mais**  
[TClink](https://tdn.totvs.com/display/tec/TClink)  
[TCunlink](https://tdn.totvs.com/display/tec/TCunlink)  
[TCConfig](https://tdn.totvs.com/display/tec/TCConfig)  
[TCRefresh](https://tdn.totvs.com/display/tec/TCRefresh)
