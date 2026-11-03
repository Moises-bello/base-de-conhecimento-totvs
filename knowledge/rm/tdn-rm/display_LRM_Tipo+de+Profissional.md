---
content_hash: 1cd2b996a6e6a609f2afa979d42578c3d82b64ec6c65218c8d1ff6e2fe5a6ea0
fetched_at: '2026-06-29T00:09:38.132283+00:00'
page_id: '425918495'
product: rm
source: tdn-rm
title: Tipo de Profissional
type: documentation
url: https://tdn.totvs.com/display/LRM/Tipo+de+Profissional
version: 2
---

Tipo de Profissional é a tabela que armazena os perfis de profissionais que serão cadastrados para atuar nos processos seletivos da instituição. Os tipos de profissionais são, por exemplo: Fiscal de Sala, Fiscal de Corredor, Fiscal de Banheiro, Porteiro, Enfermeiro, Segurança, etc. Para cada um dos tipos de profissionais também poderá ser definido um valor base de remuneração. Essa informação define o valor que será pago aos profissionais que atuarem com aquele perfil em um processo seletivo.

**Utilizações importantes**:  
 Na tabelas auxiliar "Profissional" ao cadastrar um profissional será necessário informar o perfil ou tipo do profissional que poderá ser um ou mais.

No cadastro "Local de Processo Seletivo" deverá disponibilizar quais os Tipos de profissionais que atuarão em cada local do processo seletivo. Para cada tipo disponibilizado deverá ser informada a quantidade de profissionais necessários naquela posição.

No Processo "Gerar pagamento de profissionais" o perfil do profissional e sua remuneração serão utilizados para gerar pagamentos aos funcionários que trabalharem no processo seletivo. O valor remunerado informado neste perfil é calculado por dia, ou seja, se você informar que certo perfil é remunerado em R$100.00, isso significa que sua remuneração por dia é este valor.
