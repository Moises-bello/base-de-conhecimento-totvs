---
article_id: 7090992515095
category: SIGAEST - RELATORIOS
content_hash: 98aac3262f0dd551cc1fc0d1ce8a8ceea0bf8318cd930fd65234da1ecffaec80
fetched_at: '2026-06-28T22:39:06.256297+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAEST - Mensagem ao tentar
  gerar relatório em planilha xlsx: Não foi possível encontrar C:/[...].xlsx. É possível
  que ele tenha sido movido, renomeado ou excluído?'
type: support-article
updated_at: '2025-03-12T12:42:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7090992515095-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAEST-Mensagem-ao-tentar-gerar-relat%C3%B3rio-em-planilha-xlsx-N%C3%A3o-foi-poss%C3%ADvel-encontrar-C-xlsx-%C3%89-poss%C3%ADvel-que-ele-tenha-sido-movido-renomeado-ou-exclu%C3%ADdo
---

**Ocorrência**Mensagem ao tentar gerar relatório em planilha xlsx: Não foi possível encontrar C:/[...].xlsx. É possível que ele tenha sido movido, renomeado ou excluído?

Exemplo no caso de MTR300

![mceclip0.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/7090531639191/mceclip0.jpg)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Causa**Esse incidente ocorre, geralmente, após alguma modificação nos diretórios que compõem a estrutura do ambiente Protheus.  
  
**Solução**Certifique-se de possuir o arquivo Printer.exe em todas as pastas Appserver do(s) ambiente(s). Caso não localize, copie o arquivo Printer.exe contido na pasta Smartclient e cole em todas as pastas Appserver

Caso os arquivos já estejam contidos nas pastas Appserver, outras análises que devem ser realizadas:

* O problema ocorre somente em um relatório específico? Se testar com demais relatórios o problema ocorre? Pois caso sim, o foco da análise deve ser em infraestrutura do ambiente, e em artefatos de infraestrutura (como lib/smartclient). Já se ocorrer com um relatório em específico, o foco da análise deve ser no código fonte deste relatório em questão;
* Certifique-se de estar com LIB e Smartclient atualizados;
* Verifique se o problema ocorre com um usuário em específico do Protheus, ou qualquer usuário tem o mesmo comportamento. Verifique também se ocorre testando em outro desktop/note (visto que o problema pode estar relacionado com o diretório físico);
* Abra o diretório indicado na mensagem (exemplo: C:\RELATORIOS\ ) e veja se foi gerado um arquivo nesse diretório. Caso sim, verifique se clicando com o botão direito, e em abrir, se abre diretamente no programa que executa este arquivo (exemplo: Excel) ou também não abre;
* Verifique se acionando a função Executar (exemplo: pressionando Windows+R no Windows) e digitando o programa que executa o formato xlsx (exemplo: digitar Excel) se o programa é normalmente aberto e executado.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Relatórios no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)
