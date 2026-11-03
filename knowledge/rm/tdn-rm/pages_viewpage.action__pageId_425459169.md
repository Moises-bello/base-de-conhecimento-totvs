---
content_hash: 38b0a78875eadb0a24dc7ed034dcfb89ee1a4c4749430dbba6a1d221b34784ba
fetched_at: '2026-06-29T00:09:34.492601+00:00'
page_id: '425459169'
product: rm
source: tdn-rm
title: 14.06 - Emissão de recibos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459169
version: 12
---

O objetivo desta etapa é fazer as configurações gerais da emissão de recibos das movimentações do sistema.    
   
**Configuração de recibos**   
   
**Saída padrão:** Este parâmetro define qual será a saída padrão dos recibos podendo ser através da impressora Bematech, pelo gerador de relatórios ou através de e-mails, onde os usuários recebem, no texto dos e-mails, os recibos referentes às movimentações realizadas.  
   
É possível definir se será emitido:

* **Recibo de empréstimo**
* **Recibo de renovação**
* **Recibo de devolução**
* **Recibo de multa**

Ao habilitar o a emissão de **recibo de renovação** é possível definir para**Não emitir recibo de devolução na renovação do empréstimo.** Este parâmetro define que os dados da devolução não serão exibidos no recibo de renovação e somente será válida para recibos gerados através do gerador de relatórios.  
  
  
**Recibos do gerador**  
  
O objetivo desta etapa é definir as características gerais dos recibos, quando estes são do gerador de relatórios.   
  
Nesta etapa é possível informar quais os recibos do antigo gerador ou novo gerador de relatórios que serão utilizados para empréstimo/renovação e devolução. Quando informado relatórios do novo gerador é possível parametrizar para **visualizar a impressão do relatório**. Este parâmetro não se aplica a relatórios do antigo gerador, uma vez que eles sempre serão visualizados antes da impressão.

* **OBS**: Clientes com contratos novos não poderão utilizar o Gerador de Relatório Delphi (Antigo) e deverão definir os relatórios RM Reports para a impressão dos recibos.

Importante

É possível utilizar a impressora Bematech configurada através do pool de impressão do Windows para imprimir os recibos de movimentações utilizando relatórios do RM Reports.

Neste caso é necessário ter a impressora configurada como uma impressora do Windows e definidos o tipo Gerador de relatórios nos parâmetros de emissão de recibos da biblioteca.

Se não estiver definido para visualizar antes da impressão, é necessário que a impressora esteja definida como padrão no Windows.

A TOTVS disponibiliza relatórios através book de relatórios que podem utilizados ou utilizados como modelo para criação de relatórios customizados pela instituição (Acesse: ), os relatórios estão disponíveis através do TOTVS Compartilhamento e podem ser baixados e utilizados pelas instituições.

**Recibos Bematech**

O objetivo desta etapa é definir as características gerais dos recibos, quando a saída padrão é a impressora Bematech.

Nesta etapa é definido qual a porta que será utilizada para conectar a impressora ao computador e o modelo da impressora Bematech que será utilizado.

**Imprimir página de teste:**Ao clicar nesse botão, será impressa uma página de teste, certificando que a impressora está funcionando corretamente.

**Recibos:**Este parâmetro define o número de vias dos recibos de empréstimo, de multa, renovação e devolução além do número de saltos no final dos recibos.

O TOTVS Gestão Bibliotecária suporta as seguintes impressoras:

* MP-20 MI
* MP-20 CI
* MP-20 S
* MP-2000 CI
* MP-2000 TH
* MP-2100 TH
* MP-4200 TH (após a versão 12.1.21).

Importante

*Não serão homologados novos modelos de impressoras Bematech para utilização direta no TOTVS Gestão Bibliotecária.*

Caso seja necessário, será possível configurar relatórios de empréstimos e devoluções no padrão Bematech (disponíveis através do TOTVS Compartilhamento) para impressão utilizando o gerador de relatório (descrito acima) e a impressão poderá ser feita na impressora (tipo cupom fiscal) através do driver configurado no windows.

Os relatórios abaixo foram criados no padrão Bematech e podem ser utilizados para este fim.

* BIBREL0017 - Recibo de empréstimo (padrão para impressora tipo Bematech)
* BIBREL0018 - Recibo de devolução (padrão para impressora tipo Bematech)

O TOTVS Gestão Bibliotecária permite realizar impressões com as portas:

* LPT1
* COM1
* COM2
* COM3
* COM4
* USB
* ETHERNET (apenas para a impressora MP-4200 TH).

## Configuração das impressoras MP-20 MI / MP-20 CI / MP-20 S / MP-2000 CI / MP-2000 TH / MP-2100TH

Atenção:

Para a instalação de impressoras Bematech (modelos MP-20 MI / MP-20 CI / MP-20 S / MP-2000 CI / MP-2000 TH / MP-2100TH), o sistema operacional tem que ser Windows 7 32 Bits.

Devem ser utilizadas as DLLs mp2032.dll, mp2032.lib e SiUSBXp.dll, os mesmos devem ser copiados e colados no diretório **C:\totvs\CorporeRM\RM.Net**(diretório de execução do RM.exe).

O pacote de DLLs pode ser baixado através do arquivo abaixo:

**Passo a Passo:**

Após baixar o pacote de DLL **MP2032.dll versão 4.1.6.0,**vamos copiar as DLL contidas na pasta MP2032\mp2032\Pacote DLL e colar as mesmas em **C:\totvs\CorporeRM\RM.Net**.

Agora vamos voltar no arquivo que você baixou e procurar pela pasta **Win2KXP,** que se encontra em **MP2032\mp2032\Pacote DLL\Win2kXp**.

Dentro desta pasta clique no executável Installer.exe, e prossiga com a instalação, após o termino da instalação sua impressora já estará disponível para ser utilizada.

Obs: A impressora Bematech não funciona em TS, somente local.

## Configuração da impressora MP-4200 TH

Esta impressora é suportada por sistemas operacionais 32 e 64 bits, necessário somente fazer a instalação correta do driver  e a utilização das DLLs corretas para a versão.

Para sistemas operacionais 64 bits (MP2064 - [clique aqui](https://drive.google.com/file/d/1m2IttsFADkY3HmRIaK0roZw1e0v9BCdf/view?usp=sharing) ou solicite ao suporte).

Instale o driver correto da impressora.

Copie as seguintes DLLs para a pasta **C:\totvs\CorporeRM\RM.Net**ou a pasta de execução do RM.exe

* + mp2064.dll
  + SiUSBXp.dll

**Recibos de empréstimo**  
   
O objetivo desta etapa é definir as características gerais dos recibos de empréstimo/renovação, saída padrão Bematech.   
   
**Imprimir campos:** Este parâmetro define quais campos serão apresentados no recibo impresso.  
   
**Nome da coligada no recibo (Padrão: Nome fantasia):** Este parâmetro define o nome da coligada que será impresso no recibo. Por padrão, o nome apresentado é o nome fantasia da coligada logada.  
   
**Imprimir nome da coligada condensado** e **Imprimir nome da Filial/Unidade:** Define se será impresso o nome da coligada e da filial no recibo de empréstimo/renovação.  
   
**Observações:** Este parâmetro define um texto de observações que será apresentado ao final do recibo impresso.  
   
   
**Recibos de devolução**  
   
O objetivo desta etapa é definir as características gerais dos recibos de devolução, saída padrão Bematech.   
   
**Imprimir campos:** Este parâmetro define quais campos serão apresentados no recibo impresso.  
   
**Nome da coligada no recibo (Padrão: Nome fantasia):** Este parâmetro define o nome da coligada que será impresso no recibo. Por padrão, o nome apresentado é o nome fantasia da coligada logada.  
   
**Nome da coligada no recibo (Padrão: Nome fantasia)**  
Este parâmetro define o nome da coligada que será impresso no recibo. Por padrão, o nome apresentado é o nome fantasia da coligada logada.  
   
**Imprimir nome da coligada condensado** e **Imprimir nome da Filial/Unidade:** Define se será impresso o nome da coligada e da filial no recibo de devolução.
