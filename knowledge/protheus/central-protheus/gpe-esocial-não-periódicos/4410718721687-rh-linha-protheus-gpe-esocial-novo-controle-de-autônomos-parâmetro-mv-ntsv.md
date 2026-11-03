---
article_id: 4410718721687
category: GPE - eSocial - Não Periódicos
content_hash: 5fa1080087dec318cc210b7967cdf5317b2255f86c2ef59d5486ba64027402a5
fetched_at: '2026-06-28T22:45:06.014536+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH Linha Protheus - GPE - eSocial -  Novo controle de autônomos - Parâmetro
  MV_NTSV
type: support-article
updated_at: '2026-06-16T11:52:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410718721687-RH-Linha-Protheus-GPE-eSocial-Novo-controle-de-aut%C3%B4nomos-Par%C3%A2metro-MV-NTSV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41259477750423) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Novo controle de autônomos - Parâmetro MV\_NTSV.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
De acordo com o manual do eSocial, o envio do evento S-2300 é opcional para algumas categorias de trabalhadores sem vínculo. Atualmente, os trabalhadores cadastrados com a categoria 701 ou 711 ou 712 ou 741 são enviados ao TAF caso os campos obrigatórios do eSocial estejam preenchidos, caso contrário, não é efetuado o envio do evento S-2300 para o TAF e não exibe mensagem de aviso.  
  
Esse conceito adotado não permite a opção de não enviar o evento S-2300 para o TAF.  
Foi realizada a criação do parâmetro **MV\_NTSV**.  
  
O parâmetro definirá quais categorias do eSocial não serão integrados com o TAF. Em outras palavras, o **funcionário com a categoria que estiver inserida no parâmetro não será enviado ao TAF**.  
  
**Importante**:  
O parâmetro deverá ser preenchido no padrão a seguir: **701/711/712/741** (sem aspas), ou seja, com o código da categoria do esocial (de três dígitos), seguido de barra "**/**". A configuração do exemplo indica que não haverá integração dos eventos S-2300, S-2205 e S-2399 para os funcionários com a categoria 701 ou 711 ou 712 ou 741. Se a categoria do funcionário for 721, haverá a integração dos eventos normalmente.  
  
Caso o parâmetro **não** exista ou se estiver com conteúdo **em branco**, o sistema **NÃO** efetuará integração dos eventos S-2300, S-2205 e S-2399 para os funcionários de categoria 701 ou 711 ou 712 ou 741, pois essas são as categorias que não possuem obrigatoriedade de envio para o eSocial.  
  
**Exemplos de uso:**  
1 - Parâmetro **inexistente** ou com conteúdo **em branco**:  
Sistema não irá efetuar integração dos eventos para os funcionários com a categoria 701 ou 711 ou 712 ou 741. Para o funcionário de outras categorias, por exemplo a categoria 721, a integração será efetuada normalmente.  
  
2 - Parâmetro com conteúdo **701/711/712/741**:  
Sistema não irá efetuar integração dos eventos para os funcionários com a categoria 701 ou 711 ou 712 ou 741. Para o funcionário de outras categorias, por exemplo a categoria 721, a integração será efetuada normalmente.  
  
3 - Parâmetro com conteúdo **721**:  
Sistema não irá efetuar integração dos eventos para os funcionários da categoria 721. Para o funcionário de outras categorias, por exemplo a categoria 701, a integração será efetuada normalmente.  
  
4 - Parâmetro com conteúdo **999**:  
Sistema não irá efetuar integração dos eventos para os funcionários da categoria 999. Para o funcionário de outras categorias, por exemplo a categoria 701, a integração será efetuada normalmente.  
  
**Estrutura**:

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_NTSV |
| **Tipo** | Caracter |
| **Descrição** | Informe as categorias de TSV que não são obrigados a terem o evento S-2300 |
| **Valor Padrão** | 701/711/712/741 |

**Saiba Mais**  
Acesse o boletim técnico com mais informações para solucionar sua dúvida: <https://tdn.totvs.com/pages/viewpage.action?pageId=458753479>  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "****Eventos****".*
