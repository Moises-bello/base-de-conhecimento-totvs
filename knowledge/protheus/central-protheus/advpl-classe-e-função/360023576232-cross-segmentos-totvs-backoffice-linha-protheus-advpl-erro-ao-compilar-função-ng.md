---
article_id: 360023576232
category: ADVPL - Classe e Função
content_hash: 09323c33a19142c16a3e212417054133685e427b5c237a12b0efe7aa41e94285
fetched_at: '2026-06-28T22:40:18.315886+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro ao compilar
  função NGRETCPEMP
type: support-article
updated_at: '2022-01-06T19:33:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023576232-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-ao-compilar-fun%C3%A7%C3%A3o-NGRETCPEMP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Ocorrência**

Erro ao compilar função NGRETCPEMP.  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão P12.1.17  
  
**Causa**

Mediante a uma necessidade técnica, foi realizada a retirada de algumas funções das rotinas **NGUTIL** e **MNTUTIL01**, pois estas funções não condizem com o padrão de desenvolvimento TOTVS.

**Solução**Segue abaixo as orientaçõesEm casos como fontes **específicos/customizados** ainda podem ser existir chamadas destas funções. Para estes casos, pode ser apresentado a falta de uma das funções listadas a baixo. Nestes casos deve-se abrir o documento em anexo, buscar a função e realizar a sua compilação no ambiente.

```
Atenção  
  
Somente deve ser compilada a função que está apresentado inconsistência por sua falta.  
  
Todas as funções são User Function (Funções de Usuário), por este motivo deve ser realizado   
a alteração da chamada da função nos fontes específicos, utilizando o "U_" conforme exemplo  
 a seguir: Ex. De NGRETX6() para U_NGRETX6()
```

**Saiba mais**[MNT0091 Falta de função em fontes específicos](http://tdn.totvs.com/display/public/PROT/MNT0091+Falta+de+funcao+em+fontes+especificos)
