---
article_id: 21711171003031
category: ADVPL - Classe e Função
content_hash: 51567e3cca012d716757e86f16f8faf468c59ee3f4dd739d85b8f62dde823c0d
fetched_at: '2026-06-28T22:40:18.267939+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL- Erros comuns do Printer.exe
type: support-article
updated_at: '2024-07-04T14:44:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21711171003031-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erros-comuns-do-Printer-exe
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21711157118487) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Quais os erros comuns do Printer.exe?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Causas e Soluções**

**1-** **Fwmsprinter está gerando apenas o arquivo .rel na pasta.**

**R:** Deve certificar que o caminho do arquivo está com caráteres minúsculos e verificar dentro do AppServer e SmartClient se consta o executável *TOTVS Printer* e se ele está atualizado, verifique o saiba mais para download e consulta de versão.

**2- Erro no parâmetro FwPrinterXlsx:Versão da printer.exe não suporta a geração de arquivos .xlsx. on ...**

**R:** Neste caso deve verificar a verão da printer e caso não seja a última disponível atualizar o *TOTVS Printer* e realizar o teste com o exemplo da documentação da função utilizada.

**3- O método FWMsPrinter:SayBitmap não está imprimindo a imagem.**

**R:** Valide se o caminho para imagem está correto e com caracteres minúsculos, caso esteja e ainda assim não seja impresso efetue o download da *TOTVS Printer* e atualize para lib mais recente.

**4- Após atualização de binários o sistema deixo de gerar PDF.**

**R:** Verifique se a *TOTVS Printer* consta na pasta do appserver e smartclient, caso não tenha basta efetuar o download e adicioná-la.

**5- Ao imprimir é utilizado o printer do AppServer ou o do SmartClient?**

**R:** Para impressões em que o usuário seleciona a opção de destino "Servidor", é importante ressaltar que apenas o arquivo intermediário é gerado no servidor (arquivo .rel) e desta forma a conversão final deste arquivo em pdf ocorre por meio do recurso printer.exe localizado na pasta do smartclient em execução pelo usuário.

Apenas em situações em que o componente está rodando sem interface gráfica (Exemplo: rotinas executadas via job), a conversão final do arquivo .rel em pdf ocorrerá por meio do recurso printer.exe localizada na pasta do AppServer em execução.

**Saiba Mais**

[TOTVS Printer Download](https://suporte.totvs.com/portal/p/10098/download?e=693168)

[Verificar Versão da Printer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020375572-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-verificar-a-vers%C3%A3o-da-TOTVS-printer)

[FWMsPrinter](https://tdn.totvs.com/display/public/framework/FWMsPrinter)
