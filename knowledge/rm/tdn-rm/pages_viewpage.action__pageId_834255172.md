---
content_hash: ea5f35d3b7d96fb3b3eebe3442e088b26f848617ca7e190f59fed278fb492643
fetched_at: '2026-06-29T00:11:49.478938+00:00'
page_id: '834255172'
product: rm
source: tdn-rm
title: TCGI - Cobrança - CoPilot
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=834255172
version: 5
---

A interação com a Inteligência Artificial do CoPilot já está disponível na tela de edição da Visão de Cobrança, para auxiliar na interação entre os analistas e os clientes.

Para acessar esta opção acesse o menu **Inteligência Artificial** nos anexos desta visão.

Ao acessar esta tela o sistema apresenta a seguintes opções:

* Aba **Identificação:** Esta aba apresenta os campos de parametrização da interação entre o analista e o CoPilot, a saber:
  + **Tipo de Prompt:** O tipo de prompt, que é o comando que será repassado para a de análise da IA, está fixado nesta tela com o contexto de Cobrança e não pode ser alterado;
  + **Meio de Comunicação:** Informe a origem do meio pelo qual o cliente enviou o texto a ser repassado para análise. A opções são:
    - **Email**: Quando o texto a ser analisado foi recebido por email (geralmente com uma linguagem mais formal); ou
    - **Chat:**  Quando o texto a ser analisado foi recebido por chat (geralmente com uma linguagem mais informal).
  + **Considerar os dados quantitativos dos contratos na resposta do IA:** Esta opção irá solicitar a análise dos dados quantitativos em relação à quantidade de contratos, plano de financiamento, atrasos e antecipações de parcelas e renegociações, deste cliente, que serão repassados automaticamente pelo TCGI de forma anonimizada, garantido, além do sigilo das informações, uma maior consistência na resposta e na geração do *Plano de Ação*;
  + **Mensagem (Cole aqui o retorno do cliente para análise):** Digite ou cole neste campo o interação enviada pelo cliente, de acordo com o meio de comunicação informado acima. Esta interação será enviada para análise da IA e será a base da sugestão de resposta a ser enviada para o cliente;
    - **Gerar Resposta:** Este botão enviará a interação para análise;
    - **Melhorar Resposta:** Esta opção reenviará a interação para análise solicitando que a resposta seja mais clara e mais completa, podendo ou não ser uma abordagem melhor que a da resposta anterior;
    - **Limpar Resposta:** Utilize esta opção para descartar a resposta recebida, caso deseje solicitar uma nova análise da mensagem acima;
    - Copiar Resposta: Utilize esta opção para copiar a resposta recebida para a área de transferência do sistema operacional, para poder colá-la em outra aplicação
* Aba **Resposta:** Nesta aba, temos o retorno da análise realizada pelo CoPilot da Cobrança, onde são apresentados as seguintes informações:
  + **Temperatura Emocional:** O sistema avalia a temperatura emocional do e-mail para que a resposta sugerida seja mais adequada a cada um dos cenários apresentados. Veja no quadro ao final desta documentação a importância desta informação;
  + **Resposta:** Neste campo é apresentada a resposta sugerida para o e-mail do cliente. O sistema sempre utilizará um tomcordial, profissional, educado, para tratar para com o cliente. É importante frisar que esta resposta deve ser validada e revisada, antes de ser enviada ao destinatário.
* Aba **Plano de Ação:** Neste campo são apresentadas as sugestões do Plano de Ação que pode-se adotar para interagir em relação à interação com o Cliente. As informações deste campo podem ser editadas, modificadas, incluídas, excluídas e salvas, de forma que atendam ao cenário proposto. Cada ação apresentada contém os seguintes campos:
  + **Tipo de Plano de Ação:** É a forma de ação sugerida. Exemplo: Agendamento de Reunião, Análise de Situação Contratual, Apresentação de Opções Financeiras, etc.;
  + **Plano de Ação:** É o detalhamento da sugestão de ação proposta. Caso aceito, sugerimos aos usuários que a editem e detalhem o máximo o possível, atribuindo papeis e nomes;
  + **Data de Conclusão:** É a data para a conclusão desta ação.

Importante!

A análise da **Temperatura Emocional** das conversas com clientes é essencial para compreender o estado emocional e a urgência com que cada cliente percebe a sua situação. Essa análise permite ajustar o tom e a abordagem das respostas para melhor atender às necessidades e expectativas dos clientes, visando resolver os problemas de maneira mais eficiente e empática. Vamos detalhar a importância e a utilidade desta informação em cada cenário mencionado:

1. **Cliente com temperatura emocional moderada**:

   * **Importância**: Clientes com uma temperatura emocional moderada estão conscientes de suas dívidas, mas estão abertos ao diálogo e à negociação. Eles buscam uma solução sem conflitos e esperam ser tratados com respeito.
   * **Utilidade para resposta**: Uma resposta adequada aqui deve ser empática, oferecendo suporte e soluções práticas para a resolução do problema financeiro, sem pressão excessiva. Por exemplo, propor um plano de pagamento parcelado ou uma reunião para discutir alternativas pode ser eficaz.
2. **Cliente com temperatura emocional alta**:

   * **Importância**: Quando a temperatura emocional é alta, o cliente está muito irritado e sente que está sendo tratado de maneira injusta ou excessivamente agressiva. Isso pode prejudicar a relação com a empresa se não for tratado corretamente.
   * **Utilidade para resposta**: A resposta deve reconhecer a frustração do cliente, demonstrar empatia e oferecer uma solução rápida para reduzir o número de cobranças. É crucial garantir que o cliente se sinta ouvido e respeitado, para evitar escalonamentos para reclamações formais ou ações legais.
3. **Cliente com temperatura emocional extremamente alta e melancólica**:

   * **Importância**: Este cliente está em um estado de grande vulnerabilidade emocional e financeira. A abordagem inadequada pode agravar seu estado emocional e levar a situações críticas, como crises de saúde mental.
   * **Utilidade para resposta**: A resposta deve ser extremamente sensível e empática, reconhecendo o sofrimento do cliente e oferecendo ajuda concreta. Pode incluir a suspensão temporária das cobranças, a proposta de um plano de pagamento personalizado, ou até a indicação de recursos adicionais para apoio financeiro ou emocional. A prioridade é mostrar que a empresa se preocupa com o bem-estar do cliente.

### Benefícios da Análise da Temperatura Emocional:

1. **Melhora na Relação com o Cliente**: Responder adequadamente às emoções dos clientes pode fortalecer a relação, demonstrando que a empresa é compreensiva e responsável.
2. **Prevenção de Conflitos**: Abordar as reclamações de forma apropriada pode evitar escalonamentos desnecessários, incluindo queixas formais ou ações legais.
3. **Fidelização do Cliente**: Clientes que se sentem bem tratados, mesmo em situações adversas, têm maior probabilidade de permanecer leais à empresa.
4. **Reputação da Empresa**: Um atendimento ao cliente eficaz e empático melhora a imagem da empresa no mercado, atraindo novos clientes e mantendo os atuais satisfeitos.
5. **Eficiência na Solução de Problemas**: Adaptar as respostas às necessidades emocionais do cliente pode resultar em uma resolução mais rápida e eficaz dos problemas financeiros, beneficiando ambas as partes.

Ao entender a temperatura emocional dos clientes e responder de acordo, as empresas podem oferecer um atendimento mais humanizado e eficiente, promovendo uma experiência positiva mesmo em situações desafiadoras.
