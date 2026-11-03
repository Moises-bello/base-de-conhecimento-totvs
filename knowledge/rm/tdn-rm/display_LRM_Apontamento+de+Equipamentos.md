---
content_hash: d915573fa089cb12a2deb88df687f8335de408e5d52f06fa87f1cac5516a163f
fetched_at: '2026-06-29T00:11:55.934969+00:00'
page_id: '864986116'
product: rm
source: tdn-rm
title: Apontamento de Equipamentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Apontamento+de+Equipamentos
version: 11
---

O **apontamento de equipamentos** numa obra refere-se ao registro detalhado do uso e do desempenho das máquinas e equipamentos no canteiro de obras.

Esse processo é essencial para o controle e a gestão eficaz dos recursos, garantindo que o uso dos equipamentos seja otimizado, e que o planejamento da obra seja cumprido.

Os coletores móveis recolhem os apontamentos de Equipamentos e enviam a carga com estes dados para o TOTVS Construção Obras e Projetos.

Para saber mais como realizar o apontamento de Equipamentos no app acesse: **App Minha Obra:  [Guia de Uso - Minha Obra#sobre-funcionalidades-interfaces](https://tdn.totvs.com/display/MOBILE/Guia+de+Uso+-+Minha+Obra#GuiadeUsoMinhaObra-sobre-funcionalidades-interfaces)**

**Para acessar os  Apontamentos de Equipamentos:**

* Acesse a opção de Menu: Projetos \ Construção e Projetos \ Controle \ Minha Obra\Equipamentos;

Nesse caminho é possivel visualizar todos os apontamentos com as seguintes informações:

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Mobilidade \ Equipamentos \ Apontamentos de Equipamentos;
* O cadastro de apontamentos é disponível apenas para leitura e edição, ou seja, não será possível adicionar itens manualmente, e a exclusão somente é permitida para apontamentos com status pendente;
* O Apontamento recebido do coletor terá seu status como "Pendente" quando houver alguma informação incorreta ou faltando.
* E permanecerá com esse status "Pendente" enquanto ainda estiver disponível para edição.
* Ao executar o processo "Apropriar custos" o apontamento deixa de ter status "Pendente"e passa ter status "Apropriado".(Sempre terá que executar o processo Apropriar custospois não ocorre apropriação de forma automática)
* Neste cadastro será possível visualizar e alterar algumas informações recebidas dos coletores;
* A seguir são listadas algumas das informações que estarão disponíveis para visualização:
* **Aba Apontamento de Equipamentos**

1. Nome do Coletor: Nome do coletor parametrizado na configuração do TCOP com app Minha Obra.
2. Centro de custo;
3. Tarefa: Nesse campo será exibido tarefa caso esteja parametrizado para apontar em Planilha de atividades e será exibido item caso seja parametrizado para utilizar Planilha Executiva. Veja os detalhes em:
4. Patrimônio: Bem vinculado no insumo do apontamento.
5. Descrição do Patrimônio: Descrição do Bem vinculado no insumo do apontamento.
6. Motivo de Improdutividade: Motivo que o bem ficou parado ou inativo.
7. Data/Hora Início;
8. Data/Hora Fim;
9. Status: status do apontamento
10. Motivo de inconsistência.
11. Id. Apontamento
12. Horímetro Inicial
13. Horímetro Final
14. Código da Tarefa
15. Nome da Tarefa
16. Observação Início
17. Observação Fim
18. Quilometragem Inicial
19. Quilometragem Final
20. Turno: Turno que o apontamento foi realizado.

* **Mapa**
  + Localização do apontamento  |
* **Campos Complementares**
  + Campos para auxiliar e detalhar melhor o apontamento
* Com relação à edição, somente registros que tenham status “Pendente” poderão ser editados. Além disso, as definições de quais campos serão editáveis, será de acordo com o valor do parâmetro “Integrado com SIGA-MNT”, conforme mostrado a seguir:

  + Parâmetro “Integrado com SIGA-MNT” habilitado: Todos os campos estarão bloqueados;
  + Parâmetro “Integrado com SIGA-MNT” desabilitado:

    - Tarefa;
    - Centro de custo;
    - Equipamento;
    - Motivo de Improdutividade;
    - Data/Hora Início;
    - Data/Hora Fim.
    - Quilometragem Inicial
    - Quilometragem Final
    - Horímetro Inicial
    - Horímetro Final
  + O campo horas apontadas será igual à Data/Hora Início – Data/Hora Fim;
  + O campo status pode assumir um dos seguintes valores:

    - Pendente: o apontamento “chegou” do coletor;
    - Enviado: o apontamento foi enviado para o Manutenção de Ativos;
    - Apropriado: foi gerada apropriação para o apontamento.

* **Importante:**

  + - **Caso o campo centro de custo esteja preenchido, só será possível selecionar tarefas que estejam associadas ao centro de custo informado;**
    - **No coletor somente é permitido inserir apontamentos onde a data do mesmo está no intervalo do projeto que foi definido no cronograma.**

Para que o processo de apontamento de Equipamentos funcione corretamente é importante verificar a parametrização miníma . Saiba mais em:  |  | [Parâmetros Equipamento](https://tdn.totvs.com/pages/viewpage.action?pageId=864989807)

No apontamento de Equipamentos é possivel informar motivos de improdutividade :

 (Processos)

[Apropriar Custos](https://tdn.totvs.com/display/LRM/Apropriar+Custos)

[Enviar Apontamentos para o Manutenção de Ativos](https://tdn.totvs.com/pages/viewpage.action?pageId=864986537)
