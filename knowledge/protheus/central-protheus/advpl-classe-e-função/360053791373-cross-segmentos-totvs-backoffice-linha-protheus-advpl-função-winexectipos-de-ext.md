---
article_id: 360053791373
category: ADVPL - Classe e Função
content_hash: bec5951cc067c9906a87752ed3f9003ddfa887c525e64e91be2e692c8261a23a
fetched_at: '2026-06-28T22:40:19.466479+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Função WinExec:Tipos
  de extensão válidas
type: support-article
updated_at: '2022-01-10T22:18:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053791373-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-WinExec-Tipos-de-extens%C3%A3o-v%C3%A1lidas
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**A função WinExec() não está abrindo arquivos .exe, qual o motivo?

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17

**Solução**A função **WinExec** não abre diretamente arquivos de dados de nenhum tipo, ela apenas repassa ao **SO** uma linha de comando na estação onde o **SmartClient** está em execução, ou seja, equivale a digitar diretamente uma linha de comando no *prompt* do console. Portanto apenas comandos e chamadas de aplicação  que seriam válidos nestes contexto são permitidos, como: 

```
WinExec ("DIR C:\TEMP\*.TXT")  // executa um dir  
WinExec ("CALC.EXE")    // chama a calculadora 
```

Exemplo; **"C:\Dir\teste.xls"** é apenas um nome de arquivo, não é um comando ou aplicação válida no prompt, portanto não irá funcionar.  
Já a **ShellExecute** opera de forma bem diferente, pois possui diversos parâmetros adicionais que indicam qual a ação deverá ser feita e outras opções (como por exemplo, "*Open*").   
  
**Saiba mais**[WinExec](https://tdn.totvs.com/display/tec/WinExec)
