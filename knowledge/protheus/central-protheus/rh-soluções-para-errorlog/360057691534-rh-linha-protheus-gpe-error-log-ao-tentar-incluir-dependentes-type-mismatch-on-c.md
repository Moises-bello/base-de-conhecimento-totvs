---
article_id: 360057691534
category: RH - Soluções para error.log
content_hash: 83b1c0afb9f5d945413b26b10cf168e5f466d434ae3121495a620e372bab34a4
fetched_at: '2026-06-28T22:44:08.920090+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Error log ao tentar incluir Dependentes - type
  mismatch on compare on FGP23CONS(GPEM023.PRW)
type: support-article
updated_at: '2025-08-05T14:47:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057691534-RH-Linha-Protheus-GPE-Error-log-ao-tentar-incluir-Dependentes-type-mismatch-on-compare-on-FGP23CONS-GPEM023-PRW
---

**Ocorrência**  
Ao tentar realizar a inclusão de Dependentes de um Funcionário, através da rotina **GPEA020**, é apresentado o seguinte ***error log**: **type mismatch on compare on FGP23CONS(GPEM023.PRW)***  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - todas as versões  
  
**Causa**Este erro ocorre devido a incorreta configuração do parâmetro **MV\_RHTAF**  
  
**Solução**Para solucionar esta ocorrência realize o processo conforme descrito abaixo:  
  
**1.** Acesse o **Configurador(SIGACFG) e clique em OK:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33958789190679)  
  
**2.** Acesse a rotina de **Base de Dados/Dicionário/Base de Dados**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33958789192727)  
  
**3.** Acesse o caminho Abrir a Empresa e selecione em Parâmetros:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33958789194263)  
  
**4.** Clique em Parâmetros e opte pela Lupa, conforme abaixo:   
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33958789195671)**  
  
Pesquise na seção '**Procurar por:**' informando o parâmetro **MV\_RHTAF** e depois clicar em **'Buscar' conforme abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33958789201559)**  
Após **'Buscar'** o parâmetro clique na opção da **'Lupa com uma folha(Visualizar)', conforme abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33958789202455)****5.** Após filtrar o parâmetro verifique se o mesmo se encontra conforme demonstrado no print abaixo:  
O tipo deve constar como **3-Lógico** e o conteúdo deve ser **.T.(Verdadeiro) ou .F.(Falso):**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33958805456023)  
  
**Obs.:** Verifique o parâmetro em todas as Filiais e Empresas que possuir em seu ambiente, não apenas na empresa/filial em que o erro ocorreu  
  
**Saiba mais:**  
[Pacote Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Soluções para error log](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115003853987-RH-Solu%C3%A7%C3%B5es-para-error-log)
