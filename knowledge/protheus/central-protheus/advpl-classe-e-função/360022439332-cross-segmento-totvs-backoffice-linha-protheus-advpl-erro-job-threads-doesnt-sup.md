---
article_id: 360022439332
category: ADVPL - Classe e Função
content_hash: bf9a11d68ddf650e40b3b587455e8f5f7529a8a02100342b07085ad0ccf53d6f
fetched_at: '2026-06-28T22:40:16.677691+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro: job threads
  doesn''t support remoto/visual components'
type: support-article
updated_at: '2022-11-29T21:26:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022439332-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-job-threads-doesn-t-support-remoto-visual-components
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:04:00 min  
  
Ocorrência**Ao executar qualquer função que realize a exibição de componentes gráficos em *jobs* ou *web services*, o erro abaixo é gerado:

```
JOB threads doesn't support remote/visual components
```

Contudo, em binários anteriores este erro não era gerado (ex: função MostraErro()).  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**Em binários anteriores, o sistema tentava efetuar a abertura da interface gráfica, contudo caso não conseguisse, ele gera o erro internamente e prosseguia com o processamento das demais tarefas.

Contudo, este processo poderia gerar travamentos nas rotinas e impossibilitar o prosseguimento das demais operações, retendo uma thread e onerando a operação.  
  
**Solução**Foi implementado em nível de binário uma proteção para *threads* em *status* de *job* (onde IsBlind() retorna .T.).  
Com esta proteção, no momento em que ocorrer a tentativa de exibição de um componente gráfico, será gerado o erro fatal descrito neste documento.  
Quanto as funções de exibição de interface gráfica (ex: MostraErro()), podem ser empregue o uso da função IsBlind(), pois uma vez que retornado .T., deve-se ser feito o tratamento para não exibição do componente.  
  
**Fonte**

```
/** ROTINA AUTOMÁTICA EXECUTADA ACIMA **/  
  
// VALIDAÇÃO DE ERRO NA ROTINA  
If (!lMsErroAuto) // OPERAÇÃO FOI EXECUTADA COM SUCESSO  
    ConOut(PadC("Automatic routine successfully ended", 80))  
Else // OPERAÇÃO EXECUTADA COM ERRO  
    If (!IsBlind()) // COM INTERFACE GRÁFICA  
        MostraErro()  
    Else // EM ESTADO DE JOB  
        cError := MostraErro("/dirdoc", "error.log") // ARMAZENA A MENSAGEM DE ERRO  
  
        ConOut(PadC("Automatic routine ended with error", 80))  
        ConOut("Error: "+ cError)  
    EndIf  
EndIf  
  
/** DEMAIS PROCESSO EXECUTADO PELO FONTE **/
```

**Saiba mais**  
[Proteção para thread JOB não criar interface - NG](http://tdn.totvs.com/pages/viewpage.action?pageId=417696633)  
[IsBlind - Interface com usuário](http://tdn.totvs.com/pages/releaseview.action?pageId=6814878)
