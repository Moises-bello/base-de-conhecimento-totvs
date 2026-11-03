---
content_hash: cbc4faa4991ec071d1312cecfe8cf86c589ce8f76a3c150d472337f61da72fa6
fetched_at: '2026-06-29T00:08:19.553585+00:00'
page_id: '267792921'
product: rm
source: tdn-rm
title: GLB0002_Planilha_Excel_Em_SmartClient
type: documentation
url: https://tdn.totvs.com/display/LRM/GLB0002_Planilha_Excel_Em_SmartClient
version: 7
---

# PLANILHA EXCEL EM SMARTCLIENT

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 12.1.14 |
| **Ocorrência:** | É aconselhável a utilização da planilha RM em vez da planilha Excel. |
| **Ambiente:** | Planilha.Net |
| **Informações:** | É aconselhável que o cliente utilize a planilha RM em vez da planilha Excel.  Ao tentar utilizar uma planilha Excel o sistema poderá emitir uma mensagem contendo os dizeres abaixo: Mensagem Não foi possível abrir a planilha.  A TOTVS sugere utilizar a planilha RM por possuir maior desempenho, estabilidade e melhor integração com os recursos disponíveis no RM.  É possível converter uma planilha existente em planilha RM. O processo de conversão é simples, sendo necessário apenas acessar a ferramenta 'Converter planilha Excel para planilha RM' disponível em 'Processos'.  IMPORTANTE:  A versão SmartClient do RM não suportará o uso de planilha Excel, uma vez que será substituída pela planilha RM.   Caso esteja em uma instalação local em uma máquina nova, execute (ou peça ao Administrador da Rede) o **RM.exe como administrador pelo menos uma vez**. Pois é necessário ter nível de acesso de um usuário elevado para registrar as dll's da planilha .Net no Windows.  Para acessar o processo de conversão de planilha acesso "Processos | Converter planilha Excel para planilha RM", conforme a ilustração abaixo:  Para o correto funcionamento da planilha Excel em ambiente "Smart Client" é necessário que o arquivo "**RM.Glb.PlanilhaNet.API.dll.config**" esteja presente no servidor de atualização e no Client, com as configurações conforme ilustração abaixo:      Após logar no RM e selecionar uma planilha Excel para ser aberta, verifique que será apresentada um "**Instalador do Microsoft Office**" (imagem ilustrativa abaixo), é necessário que seja instalado para que a planilha seja aberta.      Verifique que após a instalação a planilha é aberta corretamente. |
| **Observações:** |  |
