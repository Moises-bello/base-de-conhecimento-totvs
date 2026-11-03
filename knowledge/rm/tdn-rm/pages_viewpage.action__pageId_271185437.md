---
content_hash: 01f987384e52dedcab44276963abff3fd2323912cf3ab1c30035b64f13f66612
fetched_at: '2026-06-29T00:08:26.619223+00:00'
page_id: '271185437'
product: rm
source: tdn-rm
title: Renovação e aplicação dos novos arquivos de licença
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271185437
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | License Server Hardlock |
| **Versões:** | 11.XX |
| **Ocorrência:** | Renovação e aplicação dos novos arquivos de licença |
| **Ambiente:** |  |
| **Passo a passo:** | Solicitando novos arquivos de licença Para solicitar a renovação dos arquivos de licença, entre em contato com a equipe do CST (Centro de Serviços Totvs), equipe responsável pela geração dos arquivos, através do telefone (11) 4003-0015, opção 4 (Serviços Administrativos e Financeiros – CST).     Poderá também, abrir um chamado para o sertor CST / Senhas, com assunto "Renovação de arquivos de licença", informando o número de série do Hard Lock.  O número de série do Hard Lock pode ser confirmado através da etiqueta adesiva colada junto ao Token ou através do Totvs License Monitor (aplicativo do License Server), na parte inferior da tela à esquerda (Número de Série do HL). Os mesmos irão lhe enviar os novos arquivos.   Ou ainda através do Autoatendimento no site da Totvs:  Acesse o portal de [Suporte](https://totvscst.zendesk.com/hc/pt-br#home) do cliente utilizando o usuário **ADMINISTRADOR** do portal e selecione a opção "**Centro de Serviços"**:      Selecione a opção "**Liberação de acesso**" clique em "**Liberação de acesso com Hardlock**" :      Selecione a opção "**Solicitar**" :      Após isso vai ser enviado um e-mail com os arquivos de licença **(TOTVSLIC.KEY e APPLYLIC.KEY)**   Aplicando novos arquivos de licença Após o recebimento dos arquivos, favor seguir os procedimentos abaixo para atualização dos arquivos:   Informe aos usuários que o Sistema ficará indisponível;  *Após efetuar login como administrador da máquina, acesse os **SERVIÇOS DO WINDOWS** Digitando no Menu executar: **Services.msc***          *Encontre o Serviço do License Server:*          Ao clicar duas vezes sobre o serviço é apresentado o status do serviço. Assim para realizar o procedimento, Clique em **PARAR** o Serviço do License Server:          Após parar o Serviço do License Server, acesse o diretório C:\TOTVSLICENSE\BIN e faça o backup dos arquivos de licenças originais por medida de segurança. Caso haja algum problema com os novos arquivos, estes serão retornados para a pasta BIN:     Totvslic.key e Applylic.key     Confira se o número que consta nos arquivos de licença recebidos, TOTVSlic\_2100010692.key e applylic\_2100010692.key são iguais ao do Hard lock:  Após a conferir os números, renomeie os novos arquivos de licença recebidos como o exemplo abaixo:  TOTVSlic\_2100010692.key                                  TOTVSlic.key  applylic\_2100010692.key                                    applylic.key     Após renomear, coloque os arquivos no diretório: **C:\TOTVSLICENSE\BIN.**     Assim que concluído, **INICIE** novamente o Serviço do License Server:       Acesse o aplicativo TOTVS License Monitor para verificar se os arquivos de licença estão sendo lidas corretamente.   Para acessar o aplicativo Totvs Monitor, acesse a máquina cujo License Server está instalado (com o HardLock plugado), acesse o Menu Iniciar -> Todos os Programas -> Totvs License -> Totvs License Monitor.    Na tela de parâmetros inicias que será exibida não há necessidade de alteração. Basta clicar em ok. Na tela seguinte as licenças poderão ser visualizadas. |
| **Observações:** |  |
