---
article_id: 9936729584151
category: DASHBOARD
content_hash: ae196bf5b63a0ac1802c51a095725423f28eed1dfe3e7eb358e40724252e7fe9
fetched_at: '2026-06-28T22:44:41.379750+00:00'
product: protheus
section_id: 10299521604759
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como utilizar o nome social no MEU RH
type: support-article
updated_at: '2026-03-20T14:27:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9936729584151-RH-Linha-Protheus-MEU-RH-Como-utilizar-o-nome-social-no-MEU-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28220063403671) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Aplicativo não apresenta o nome social do funcionário  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - MEU RH - Todas as versões  
  
**Causa**  
Falta do parâmetro e atualização para uso desse recurso  
  
**Solução**  
**Passo 1:**  
Para que seja contemplado essa opção, é necessário estar com último pacote de Expedição Contínua do RH aplicado no ambiente assim como os arquivos do portal MEU RH:  
-> [**Como fazer o download do pacote de expedição contínua (Acumulado) do RH Protheus**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
-> [**Arquivos do portal MEU RH**](https://suporte.totvs.com/portal/p/10098/download?e=696055)  
  
**Passo 2:**  
Criar o parâmetro **MV\_NOMESOC** do tipo lógico e deixar o conteúdo do mesmo "**.T.**" sem as aspas e **reiniciar o serviço do REST** para contemplar o novo parâmetro criado.  
  
Todos os funcionários que tiverem preenchido o nome social em seu cadastro (**Tabela SRA - RA\_NSOCIAL**), conseguirá visualiza-lo no ambiente do Meu RH. A visualização do nome social, acontece nos seguintes locais:  
  
**Para os funcionários visualizando seu nome social:**  
- Início.  
- Envelope de pagamento.  
- Recibo de férias.  
- Aviso de férias.  
- Aniversariantes do mês.

**Para os gestores visualizando o nome social de seus colaboradores:**  
- Notificações de aprovação.  
- Organograma.  
- Gestão do Time.  
- Gestão de Férias.  
- Solicitar substituto.  
- Aniversariantes do mês.  
- Requisições.

**Saiba Mais  
[Documento da Melhoria](https://tdn.totvs.com/display/NPR/DT+DRHMEURH-7182+Exibir+o+nome+social+do+colaborador)****[RH - Linha Protheus - MEU RH - Aprenda sobre o MEU RH e como fazer a implantação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164214)  
[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)[para acessar mais artigos e FAQs sobre o MEU RH](%20https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)[para acessar a documentação de referência sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
