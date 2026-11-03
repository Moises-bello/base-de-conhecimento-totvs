---
article_id: 41104133754263
category: GPE - eSocial - Periódicos
content_hash: 8775dbe18aaea764eed94d751a04c5ac18cb31fa8b6e0b2dab54b7524a67d72a
fetched_at: '2026-06-28T22:45:07.593537+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Rubricas de Férias e Abono Salarial (PIS)
type: support-article
updated_at: '2026-06-18T18:48:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41104133754263-RH-Linha-Protheus-GPE-eSocial-Rubricas-de-F%C3%A9rias-e-Abono-Salarial-PIS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41104133741591) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como corrigir possíveis divergências relacionadas ao pagamento do Abono Salarial (PIS)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Com base no [Manual de Orientações para o Abono Salarial](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/trabalhador/abono-salarial/manual-de-orientacao-para-o-empregador-atualizado-22-05.pdf) e após identificar a possibilidade de duplicação dos valores de férias para esse fim, foi disponibilizada a rotina **GPEM948 Inconsistências Férias - Abono Salarial** para consulta e tratamento destas informações.  
  
No calendário de pagamento de 2026, terão direito ao benefício os trabalhadores que atenderem aos critérios abaixo:

- ter recebido, no ano-base 2024, remuneração média mensal de até R$ 2.766,00;  
- ter exercido atividade remunerada por, no mínimo, 30 (trinta) dias, consecutivos ou não, no ano-base;  
- estar cadastrado há pelo menos 5 (cinco) anos no Fundo de Participação PIS-Pasep, contados da data da primeira admissão com empregador contribuinte para o Programa.  
  
**Passo a Passo:**  
  
**1º) Atualização do ambiente:**  
Aplicar o pacote disponível no link <https://tdn.totvs.com/pages/releaseview.action?pageId=1073762340>;  
Atualizar o Dicionário de Dados contido no pacote [Expedição Continua RH](https://tdn.totvs.com/pages/releaseview.action?pageId=501123489) e executar o UPDDISTR;  
  
**2º)** Incluir a rotina a rotina **GPEM948**no Menu do **SIGAGPE**no caminho **Miscelânea > eSocial > Inconsistências Férias - Abono Salarial** (função Protheus);  
  
**3º)** No cadastro de **Verbas** (GPEA040), criar uma nova verba, do tipo 4-Informativa Dedutora, **ID 1987**, natureza 1016, incidência 11 para INSS, 00 para FGTS e 9 para IRRF e enviar essa verba com inicio de validade 01/2024;  
  
**4º)** Após os procedimentos acima, acesse a nova rotina e siga os passos a seguir:  
  
Preencher as Perguntas:

**Atenção**, utilizamos o ano de 2025 no print abaixo apenas como teste para mostrar o funcionamento da rotina, para **entrega até dia 20/06/2026 devem informar 2024.**

O governo ainda não disponibilizou o valor da media mensal para 2025.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41104103225879)  
  
 devem informar Os parâmetros de matrícula, CPF, Centro de Custo serão ignorados quando ambos estiverem em branco.  
  
**ATENÇÃO - TETO A SER CONSIDERADO**  
Inclua no campo "**Teto Pis a Considerar/Média**" o valor de R$ 2.766,00, conforme manual do PIS, esse valor não é exatamente o dobro do salário mínimo, mas é a determinação do eSocial.  
  
O padrão é apresentar somente funcionários que estão acima da média para recebimento do PIS, devido ao valor da verba de férias (Natureza 1016) estar duplicado no total de remunerações, caso queira visualizar todos os funcionários, mesmo aqueles que não se enquadram nesse cenário, alterar a pergunta “**Apenas Func. a ajustar**” para Não.  
  
**Observação**: Ao responder "Sim" à pergunta "**Apenas Func. a ajustar**", serão listados apenas os funcionários que realmente necessitam de ajuste. Os funcionários cuja **Remun. Média Atual** seja inferior ao teto de R$ 2766,00 não serão apresentados na rotina.  
  
**Exemplo**: Um funcionário possui Remun. Média Atual de R$ 2.500,00. Com esse valor, ele atende aos critérios para recebimento do Abono Salarial, não sendo necessária a retificação do evento S-1200. Nesse cenário, o sistema não o considerará caso a pergunta esteja parametrizada com a opção "Sim".  
  
**5º)** Após confirmação, será apresentada a tela abaixo, clicar em**CARREGAR FUNCIONÁRIOS**

**Atenção**, utilizamos o ano de 2025 no print abaixo apenas como teste para mostrar o funcionamento da rotina, para **entrega até dia 20/06/2026 devem informar 2024.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41104133742487)  
  
Por padrão, todos os funcionários vêm marcados. Em Outras Ações, é possível desmarcá-los.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41104103228823)  
  
No exemplo abaixo, a remuneração média correta é de R$ 2.644,16. Entretanto, o sistema está considerando a média de R$ 2.952,65, valor superior ao teto do PIS. Por esse motivo, o trabalhador foi excluído do recebimento do abono salarial. É necessário ajustar o cálculo da média para garantir sua elegibilidade ao benefício.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41104133746327)  
  
Ao dar um duplo clique, é possível visualizar a memória de cálculo utilizada para apuração da média dos meses.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41104103229719)  
  
  
Confirmando a alteração, o sistema irá **ajustar o valor da verba com ID 1870 e incluir a verba com o ID 1987**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41104133747479)  
  
Exibe o log informando as alterações: Inclusão da verba AA1 (1987) e alteração da A78 (1870)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41104133748375)  
Também é realizado uma edição do evento S-1200 gerado no TAF como evento retificador  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41104103231255)  
  
**Para seguir com a transmissão do mesmo realize os passos abaixo:**  
- [Reabra o período no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025816453-RH-Linha-Protheus-GPE-eSocial-S-1298-%C3%89-poss%C3%ADvel-reabrir-o-per%C3%ADodo-no-esocial-atrav%C3%A9s-do-GPE) (envio do evento S-1298)  
- [Exclua o evento S-1210](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027742231-RH-Linha-Protheus-GPE-eSocial-S-3000-Como-realizar-a-exclus%C3%A3o-de-um-Evento-Peri%C3%B3dico-S-1200-e-S-1210?source=search)  
- Transmita o evento S-1200 retificado   
- Realize uma nova geração e transmissão do evento S-1210  
- [Envie o fechamento S-1299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022286212-RH-Linha-Protheus-GPE-eSocial-S-1299-Como-gerar-o-evento-S-1299-fechamento-peri%C3%B3dicos-para-transmitir-ao-RET)  
  
A **documentação completa** foi centralizada na pagina abaixo:  
[**PIS - Nova Sistemática**](https://tdn.totvs.com/pages/releaseview.action?pageId=1071999838)  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
