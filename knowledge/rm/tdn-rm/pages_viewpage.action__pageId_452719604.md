---
content_hash: 9687307b835bcb07094456d43757560eb0aac965e34b1bcc7a1af62c103e9ef8
fetched_at: '2026-06-29T00:10:08.908906+00:00'
page_id: '452719604'
product: rm
source: tdn-rm
title: Configurações Gerais 1/7
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719604
version: 13
---

Nesta aba é possível fazer as Configurações Gerais relacionadas ao eSocial:     
   
**Tipo de Ambiente**  
Campo onde o usuário irá informar o tipo de ambiente do eSocial, podendo ser:

**1 - Produção:** Ambiente destinado para processamento e apuração das informações do empregador que produz todos os efeitos jurídicos;  
**2 - Produção restrita:** Ambiente de teste no qual as informações do empregador não serão validadas com os sistemas externos e não produzirão efeitos jurídicos.   
**7 - Homologação**: Ambiente de teste utilizado para homologação no SERPRO.

**Atenção:** Uma vez que já tenha transmitido eventos para o governo no ambiente "1-Produção", a alteração para outro tipo de ambiente deve ser realizada apenas em casos de real necessidade, pois poderá influenciar diretamente nos dados já transmitidos.

     
**Versão do leiaute**  
Neste campo, selecionamos o leiaute que será utilizado para a geração dos XMLs e para o validador. Ficam disponíveis apenas as duas versões mais recentes do leiaute liberado pelo governo, garantindo a conformidade com as exigências atuais.

**ATENÇÃO:**

Quando liberamos uma nova Nota Técnica, a penúltima versão é removida do parametrizador. No entanto, não realizamos a exclusão no banco de dados, a penúltima versão é removida somente para que o produto mantenha sempre apenas as duas últimas versões disponíveis, garantindo a conformidade com o leiaute vigente do eSocial.

Quando isso acontece, ao processar qualquer rotina do eSocial, o sistema apresenta uma mensagem solicitando que o usuário redefina o campo “Versão do leiaute” no parametrizador, no caminho: Configurações | Parametrizador | Folha de Pagamento | eSocial | Configurações Gerais.

   
   
**Data da Obrigatoriedade/Adesão ao eSocial**  
Parametrização das datas de obrigatoriedade do envio dos eventos: Tabelas, Não Periódicos e Periódicos.

**Economia Mista**  
Marque este parâmetro quando a empresa não se enquadrar no grupo 4, ou seja, já envia funcionários em outro grupo (1, 2 ou 3), porém possui funcionários com regime próprio, o campo "Não Periódicos" deverá permanecer com a data do grupo a qual a empresa se enquadra (1, 2 ou 3), porém deverá marcar o parâmetro "Economia Mista" e preencher o campo "Não Periódicos" informando a data de "22/11/2021", assim o sistema irá considerar essa data na tratativa dos eventos não periódicos dos funcionários com categoria (3XX).

**Meses a manter na Fila de Eventos**  
Neste campo deverá ser preenchido com no mínimo 2 meses. .

**ATENÇÃO:**

As datas parametrizadas aqui serão consideradas como "base" para a validação de alguns campos existentes no layout, assim como nos processos: Carga Inicial, Gerar XML, Fila de Eventos e Integrar com o TAF.

**OBSERVAÇÕES:**

1 - Caso esteja em ambiente com o tipo "1-Produção", os processos: "Gerar XML", "Integrar com TAF"  e o acesso à "Fila de Eventos" e "Período de Apuração" serão disponibilizados conforme as datas de obrigatoriedade definidas. Assim, se o ambiente for de produção e as datas de obrigatoriedades de eventos não periódicos e periódicos forem posteriores à data atual, apenas ficarão disponíveis para a execução desses processos os eventos de tabela. Quando as datas de obrigatoriedade forem anteriores à data atual, todos os processos serão liberados para execução.  
Os eventos de Saúde e Segurança do Trabalhador (S-2210, S-2220 e S-2240) ainda não estão disponíveis no ambiente de produção, pois o governo ainda não está apto a recebe-los devido ao faseamento.  
   
2 - Caso esteja em ambiente diferente do tipo "1-Produção", será possível realizar todos os processos independente da data de obrigatoriedade.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

eSocial Parametrizador
