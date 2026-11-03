---
article_id: 16778938060567
category: PONTO ELETRÔNICO
content_hash: 2f058796a827a7cd8ac4f0422287c43b3efbf0b1cea7826084531a2c10f797c5
fetched_at: '2026-06-28T22:44:36.591905+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como gerar o Extrato de Banco de Horas pelo
  Meu RH
type: support-article
updated_at: '2025-12-16T11:44:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16778938060567-RH-Linha-Protheus-MEU-RH-Como-gerar-o-Extrato-de-Banco-de-Horas-pelo-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16778928785815) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Como gerar o Extrato de Banco de Horas pelo Meu RH?  
  
**Ambiente**  
TOTVS RH - RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**  
Temos pelo App Meu RH, a possibilidade de **gerar o Extrato do Banco de Horas** do funcionário.  
  
Para isso, é necessário seguir os seguintes passos:  
1º: Acessar o Protheus, via módulo **18 - SIGATCF**, acessar a rotina de **Permissões Meu RH - TCFA006** e, **habilitar** as opções a seguir, para o **usuário do portal vinculado ao funcionário**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16778658302615)  
  
2º: Acessar o Meu RH com o usuário e no Menu **Espelho de Ponto**, haverá **o botão Extrato de Horas**, como demonstrado a seguir:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16778708157591)  
  
3º: Ao clicar sobre a opção, será gerado um arquivo **PDF**, com os apontamentos de **Banco de Horas** do funcionário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16778761124375)  
  
Caso seja um funcionário realizando o *download* do seu próprio extrato, serão consideradas as seguintes informações:  
- **Data de início para busca do banco de horas**: Admissão do Funcionário  
- **Data fim para buscar do banco de horas**: Último dia do período em aberto.  
  
Ao final do documento, será demonstrado o **Saldo Anterior ao período aberto**, **lançamentos deste período** e **Saldo Atual**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16778829278103)  
Se for desejado a customização do Extrato de Banco de Horas no App Meu RH, será necessário compilar o ***RDMake MRHEXTBH.prw***, disponível no pacote de Expedição Contínua do GPE, pasta *RDMakes*.  
<https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO>   
  
**Saiba Mais**  
[**8.7 Download do Extrato de Horas.**](https://tdn.totvs.com/pages/viewpage.action?pageId=756456125)  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
