---
content_hash: 0e50355b10f71a7dee809173517b5e146ae26849aebd72e35d420f697e22218a
fetched_at: '2026-06-29T00:09:54.222957+00:00'
page_id: '444596281'
product: rm
source: tdn-rm
title: Comunicado DIRF 2019
type: documentation
url: https://tdn.totvs.com/display/LRM/Comunicado+DIRF+2019
version: 17
---

A secretaria da Receita Federal do Brasil promoveu alterações na DIRF 2019, entre elas destacamos as seguintes:

* O campo "Efetuou pagamentos relacionados aos Jogos Olímpicos 2016 e aos Jogos Paraolímpicos 2016" foi retirado do leiaute de 2018;
* Foi inserido o campo "Indicador de fundação pública de direito privado instituída pela União, Municípios ou Distrito Federal", este campo fica localizado nos parâmetros específicos da coligada na sub-aba de "Pessoa Jurídica". Este campo pertence ao registro DECPJ, e entra em substituição ao campo "Efetuou pagamentos relacionados aos Jogos Olímpicos 2016 e aos Jogos Paraolímpicos 2016", que foi retirado. Este campo será habilitado apenas se o campo 'Natureza do Declarante' estiver com umas das opções abaixo selecionada:

  + 1 - Órgãos, autarquias e fundações da administração pública federal;
  + 2 - Órgãos, autarquias e fundações da administração pública estadual, municipal ou do distrito federal;
  + 8 - Entidade com alteração de natureza jurídica (uso restrito).
* Foram inseridos os campos "Indicador de Declarante Falecido", "Data do Óbito", "Situação do Espólio", "CPF do Inventariante" e "Nome do Inventariante", relacionados ao óbito do declarante pessoa física, no registro DECPF. Para visualizar as regras dos campos inseridos, acesse o link  no tópico "Pessoa Física".

* O tamanho do campo "Valor Pago ao Ano" foi alterado para 9 caracteres.
* No registro 'BPFRRA – Beneficiário pessoa física do rendimento recebido acumuladamente da DIRF', foi criado o campo 'INFPA – Informações do beneficiário da pensão alimentícia', que terá associado o registro 'RTPA – Rendimentos Tributáveis – Dedução – Pensão Alimentícia' do registro ', que anteriormente era vinculado ao registro 'QTMESES – Quantidade de meses' .  
  OBS: A geração deste registro é condicionada ao campo 'Indicador de identificação do alimentando'.   
  + Se o campo 'Indicador de identificação do alimentando' igual a 'S', será gerado o registro INFPA seguido do registro de valor (RTPA e/ou ESPA) para cada alimentando.
  + Se o campo 'Indicador de identificação do alimentando' for igual a 'N' não será apresentado o registro INFPA e será gerado os registros de valores (RTPA e/ou ESPA) com o valor total de pensão alimentícia pago a todos os alimentandos do beneficiário.
  + Para que o campo "Indicador de identificação do alimentando" seja preenchido com "S" deverá ser cadastrado um histórico de RRA para o funcionário em 'Anexos | Folha de Pagamento | Histórico de RRA' e preencher o campo 'Pagamento RRA' como 'Pago pelo declarante' e para que seja preenchido com 'N', basta detalhar a pensão alimentícia paga por dependente.
  + Para maiores informações, consulte o  leiaute da DIRF 2019 (página 22).

A TOTVS sugere aos clientes que estudem desde já os impactos das alterações da DIRF 2018 em sua organização e que acompanhem novos comunicados sobre o assunto.
